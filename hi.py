import tkinter as tk
from tkinter import filedialog

# Functions

def new_letter():
    text.delete("1.0", tk.END)

def open_letter():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        with open(filename, "r") as file:
            letter = file.read()

        text.delete("1.0", tk.END)
        text.insert("1.0", letter)

def save_letter():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        letter = text.get("1.0", tk.END)

        with open(filename, "w") as file:
            file.write(letter)


# Window
root = tk.Tk()
root.title("Letter Writer")
root.geometry("700x500")

# Title
title = tk.Label(root, text="💌 Letter Writer", font=("Arial", 20))
title.grid(row=0, column=0, columnspan=3, pady=10)

# Text box
text = tk.Text(root, width=75, height=22)
text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Buttons
new_button = tk.Button(root, text="New Letter", command=new_letter)
new_button.grid(row=2, column=0, padx=10, pady=10)

open_button = tk.Button(root, text="Open Old Letter", command=open_letter)
open_button.grid(row=2, column=1, padx=10, pady=10)

save_button = tk.Button(root, text="Save As", command=save_letter)
save_button.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()