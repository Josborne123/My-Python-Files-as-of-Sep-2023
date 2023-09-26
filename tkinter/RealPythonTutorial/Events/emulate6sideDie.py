import tkinter as tk


def random():
    import random
    label["text"] = random.randint(1,6)
    

window = tk.Tk()

window.rowconfigure([0,1], minsize=50, weight=1)
window.columnconfigure(0, minsize=200, weight=1)

button = tk.Button(master=window, text="Roll", command=random)
button.grid(row=0, column=0, sticky="nsew")

label = tk.Label(master=window, text="0")
label.grid(column=0, row=1)


window.mainloop()