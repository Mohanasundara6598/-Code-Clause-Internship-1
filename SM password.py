from tkinter import *
import random
import string
window = Tk()
window.geometry("500x500")
window.title("Password Generator")
window.config(bg="blue")
password_var = StringVar()
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)


lb = Label(window, text="Welcome", font=("Verdana", 20, "bold"), fg="white", bg="blue")
lb.place(x=170, y=100)


en = Entry(window, textvariable=password_var, font=("Verdana", 20, "bold"), width=20, justify="center")
en.place(x=50, y=200)

bt = Button(window, text="Generate", width=10, font=("Verdana", 15, "bold"), bg="green", fg="white", command=lambda: generate_password(length=12))
bt.place(x=200, y=300)

window.mainloop()
