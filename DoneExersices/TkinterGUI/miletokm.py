from tkinter import *


window = Tk()
window.title("Miles to kilometers")
window.minsize(width=250, height=200)
window.config(padx=40, pady=40)

miles_label = Label(text="- Miles", font=("Arial", 18, "bold"))
miles_label.grid(column=2, row=0)
result = Label(text=0, font=("Arial", 18, "bold"))
result.grid(column=1, row=2)
km_label = Label(text="- Km", font=("Arial", 18, "bold"))
km_label.grid(row=2, column=2)



def convert_to_km():
    num_to_convert = int(entry.get())
    converted_km = num_to_convert * 1.609344
    result.config(text=f"{converted_km:.2f}")
    
    


button = Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=1)

entry = Entry(width=5)
entry.grid(column=1, row=0)














window.mainloop()