import tkinter as tk
window = tk.Tk()

button = tk.Button(
    text="Click me",
    width = 50,
    height = 25,
    bg = "darkblue",
    fg = "yellow"
)

button.pack()



window.mainloop()