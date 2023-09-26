import tkinter as tk
window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label1 = tk.Label(text="I'm in Frame A", master=frame_a)
label2 = tk.Label(text="I'm in Frame B", master=frame_b)

label1.pack()
label2.pack()

# Swap the order of `frame_a` and `frame_b`
frame_b.pack()
frame_a.pack()

window.mainloop()