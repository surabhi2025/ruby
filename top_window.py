from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Main")

#creating the top window
def topwin():

    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")


# adding a label widget
    l2 = Label(top, text="This is toplevel window")
    l2.pack()

    top.mainloop()

#adding a label and button to the main window

l = Label(root, text="This is root window")
btn = Button(root, text="click here to open another window",
command=topwin)

l.pack()
btn.pack()

root.mainloop()








