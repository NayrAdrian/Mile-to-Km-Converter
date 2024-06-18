import tkinter
from tkinter import messagebox

# Setup Window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


# Button Function
def button_calculate():
    try:
        miles = float(input.get())
        km = miles * 1.60934
        my_label_answer.config(text=round(km, 2))
    except ValueError:
        messagebox.showerror(title="Invalid input", message="Please enter a valid number")


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

my_label = tkinter.Label(text="Miles", font=("Arial", 12))
my_label.grid(column=2, row=0)
my_label.config(padx=10, pady=10)

my_label = tkinter.Label(text="is equal to", font=("Arial", 12))
my_label.grid(column=0, row=1)
my_label.config(padx=10, pady=10)

# Label that shows the converted answer
my_label_answer = tkinter.Label(text="0", font=("Arial", 12))
my_label_answer.grid(column=1, row=1)
my_label_answer.config(padx=10, pady=10)

my_label = tkinter.Label(text="Km", font=("Arial", 12))
my_label.grid(column=2, row=1)
my_label.config(padx=10, pady=10)

button = tkinter.Button(text="Calculate", command=button_calculate)
button.grid(column=1, row=2)

window.mainloop()
