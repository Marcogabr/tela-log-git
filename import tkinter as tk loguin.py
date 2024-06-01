import tkinter as tk
from tkinter import messagebox

def check_password():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Success", "Welcome, admin!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Username:")
label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

label = tk.Label(root, text="Password:")
label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

button = tk.Button(root, text="Login", command=check_password)
button.pack()

root.mainloop()