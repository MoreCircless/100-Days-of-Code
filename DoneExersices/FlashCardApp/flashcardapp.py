from tkinter import *

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
middle_cv = Canvas()
middle_cv = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
back_card = PhotoImage(file=CARD_BACK)
middle_cv.create_image(100, 100, image=back_card)
middle_cv.grid(row=0, column=0, columnspan=2)



# * Buttons
wrong = Button(window, image=WRONG, command=None)
wrong.grid(row=1,column=1)




window.mainloop()

