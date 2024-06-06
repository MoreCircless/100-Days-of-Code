from tkinter import *
import pandas as pd
import random

current_card = {}
to_learn = {}
try:
    data = pd.read_csv("DoneExersices/FlashCardApp/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("DoneExersices/FlashCardApp/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    middle_cv.itemconfig(center_image, image= front_card)
    current_card = random.choice(to_learn)
    fr_word = current_card["French"]
    middle_cv.itemconfig(card_word, text=fr_word, fill="black")
    middle_cv.itemconfig(card_title, text="French", fill="black")
    flip_timer = window.after(ms=3000, func=flip_card)
    

def flip_card():
    middle_cv.itemconfig(center_image, image= back_card)
    middle_cv.itemconfig(card_title, text="English", fill="white")
    middle_cv.itemconfig(card_word, text=current_card["English"],fill="white")
    
    

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("DoneExersices/FlashCardApp/data/words_to_learn.csv", index=False)
    next_card()
    


BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK = "/home/manu/100-Days-of-Code/DoneExersices/FlashCardApp/images/card_back.png"
CARD_FRONT = "/home/manu/100-Days-of-Code/DoneExersices/FlashCardApp/images/card_front.png"
WRONG = "/home/manu/100-Days-of-Code/DoneExersices/FlashCardApp/images/wrong.png"
RIGHT = "/home/manu/100-Days-of-Code/DoneExersices/FlashCardApp/images/right.png"

# * Window
window = Tk()
window.title("Flash Card!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# * Photos
back_card = PhotoImage(file=CARD_BACK)
front_card = PhotoImage(file=CARD_FRONT)
wrong = PhotoImage(file=WRONG)
right = PhotoImage(file=RIGHT)

# * Labels 
middle_cv = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
center_image = middle_cv.create_image(400, 263, image=front_card)
middle_cv.grid(row=0, column=0, columnspan=2)
card_title = middle_cv.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = middle_cv.create_text(400, 263, text="word", font=("Ariel", 60, "italic"))


unknown_button = Button(image=wrong, highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

check_button = Button(image=right, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

flip_timer = window.after(ms=3000, func=flip_card)
next_card()
window.mainloop()

