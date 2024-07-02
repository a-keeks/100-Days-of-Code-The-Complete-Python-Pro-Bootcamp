from tkinter import *

def button_clicked():
    my_label.config(text = get_content())

def get_content():
   #Get the content of Entry Widget
   new_entry = entry.get()
   return new_entry

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx=100, pady=200)

# Create Label
my_label = Label(text = "I am a Label", font = ("Calibri", 24, "bold"))
my_label.config(text = "New Text")
my_label.grid(column=0, row=0) #puts label on to screen
my_label.config(padx=50,pady=50)

# Button
button = Button(text = "Click Me", command = button_clicked)
button.grid(column=1,row=1)

# Entry
entry = Entry()
print(entry.get())
entry.grid(column=4, row=3)

# New Button
new_button = Button(text = "New Button", command = button_clicked)
new_button.grid(column=3,row=0)


window.mainloop()

