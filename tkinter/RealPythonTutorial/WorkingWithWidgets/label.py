from cProfile import label
import tkinter as tk
window = tk.Tk()

#label = tk.Label(text="Hello, Tkinter", foreground="lightblue", background="darkgreen")
label = tk.Label(text="Hello, Tkinter", fg="lightblue", bg="darkgreen", width=30, height=10)

label.pack()


window.mainloop()