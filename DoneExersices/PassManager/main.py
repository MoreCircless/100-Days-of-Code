from tkinter import *
from tkinter import messagebox
import random
import pyperclip

DATA_PATH = "/home/manu/100-Days-of-Code/DoneExersices/PassManager/PassData.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(1, 2)
    nr_numbers = random.randint(1, 2)
    password_list = []

    password_letters = [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    password_symbols = [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    password_numbers = [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    return password


def write_pass():
    pass_entry.delete(0, END)
    pass_entry.insert(0, gen_pass())
    messagebox.showinfo(title="Success!", message="Passsword successfully copied into you clipboard!")
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_info(data):
    with open(DATA_PATH, mode="a") as txt:
        txt.write(f"{data[0]} | {data[1]} | {data[2]} \n")
    web_entry.delete(0, END)
    pass_entry.delete(0, END)
    messagebox.showinfo(title="Success!", message=f"Password correctly save into the following path:\n{DATA_PATH}")
    
    
    
    
def get_info():
    data = []
    web = web_entry.get()
    data.append(web)
    mail_user = mail_user_entry.get()
    data.append(mail_user)
    passw = pass_entry.get()
    data.append(passw)
    
    if len(web) == 0 or len(mail_user) == 0 or len(passw) == 0:
        messagebox.showwarning(title="Error", message="Please don't leave any field empty!")
    else:
        usr_status = messagebox.askokcancel(title= web, message= f"Details:\nEmail/User: {mail_user}\nPassword: {passw}\nDo you want to save?") 
        if usr_status:
            write_info(data=data)
        
    


# ---------------------------- UI SETUP ------------------------------- #
# * Window SETUP
window = Tk()
window.title("Pass Manager!")
window.config(padx=20, pady=20, bg="white")

# * Logo SETUP
logo = PhotoImage(file="/home/manu/100-Days-of-Code/DoneExersices/PassManager/logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 112, image=logo)
canvas.grid(row=0,column=1)

# * Button SETUP
add_button = Button(text="Add", command=get_info, width=36)
add_button.grid(row=4, column=1, columnspan=2)

gen_pass_button = Button(text="Generate Password", command=write_pass)
gen_pass_button.grid(row=3, column=2)

# * Label SETUP
web_lb = Label(text="Website:", background="white", justify="right")
web_lb.grid(row=1, column=0)
mail_user_lb = Label(text="Email/Username:", background="white", justify="right")
mail_user_lb.grid(row=2, column=0)
pass_lb = Label(text="Password:", background="white", justify="right")
pass_lb.grid(row=3, column=0)

# * Entry SETUP
web_entry = Entry(width=35, justify="left")
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
mail_user_entry = Entry(width=35, justify="left")
mail_user_entry.grid(row=2, column=1, columnspan=2)
mail_user_entry.insert(0, "@mail.com")
pass_entry = Entry(width=21, justify="left")
pass_entry.grid(row=3, column=1)




window.mainloop()