import tkinter as tk
window = tk.Tk()

name_entry = tk.Entry(width=40, bg="white", fg="black")
name_entry.pack()

name_entry.insert(0, "What is your name?")




window.mainloop()