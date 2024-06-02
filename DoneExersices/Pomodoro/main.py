from tkinter import *
import math



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    textlabel.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
    



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        textlabel.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        textlabel.config(text="Break", fg=RED)
    else:
        textlabel.config(text="Focus", fg=PINK)
        count_down(work_sec)
    
    
    
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_min < 10:
        if count_sec < 10:
            canvas.itemconfig(timer_text, text=f"0{count_min}:0{count_sec}")
        else: 
            canvas.itemconfig(timer_text, text=f"0{count_min}:{count_sec}")

    else: 
        if count_sec < 10:
            canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
        else: 
            canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")


    if count >=  0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
        
            
    










# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
textlabel = Label(text="Timer", background=YELLOW, fg=GREEN, font=(FONT_NAME, 60, "bold"))
textlabel.grid(row=0, column=1)




startbutton = Button(text="Start", command=start_timer)
startbutton.grid(row=3, column=0)


resetbutton = Button(text="Reset", command=reset_timer)
resetbutton.grid(row=3, column=3)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


tomato = PhotoImage(file="/home/manu/100-Days-of-Code/DoneExersices/Pomodoro/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)



window.mainloop()















