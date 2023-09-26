import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

def opening_screen():

    def fahrenheight_btn():
        greeting.destroy()
        buttons.destroy()
        fahrenheight_chosen()

    def kelvin_btn():
        greeting.destroy()
        buttons.destroy()
        kelvin_chosen()

    greeting = tk.Frame(master=window, width=50, height=10)
    buttons = tk.Frame(master=window, width=50, height=30, pady=10)

    window.columnconfigure([0,1], minsize=15, weight=1)
    window.rowconfigure(1, minsize=15, weight=1)

    lbl_choose = tk.Label(master=greeting, text="Choose one of the below to convert into Celsius")
    btn_fahrenheight = tk.Button(master=buttons, text="Fahrenheight", command=fahrenheight_btn, width=15, relief="raised")
    btn_kelvin = tk.Button(master=buttons, text="Kelvin", command=kelvin_btn, width=15, relief="raised")

    greeting.grid()
    buttons.grid()
    lbl_choose.grid()
    btn_fahrenheight.grid(row=1, column=0, sticky="ew")
    btn_kelvin.grid(row=1, column=1, sticky="ew")

opening_screen()

def fahrenheight_chosen():

    def f_to_c():
        """Convert the value for Fahrenheit to Celsius and insert the result into label_result"""
        fahrenheight = entry_temperature.get()
        celsius = (5/9) * (float(fahrenheight) - 32)
        label_result["text"] = f"{round(celsius,2)} \N{DEGREE CELSIUS}"

    frame_entry = tk.Frame(master=window)
    entry_temperature = tk.Entry(master=frame_entry, width=10)
    label_temp = tk.Label(master=frame_entry, text="\N{DEGREE FAHRENHEIT}")
    btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=f_to_c)
    label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

    def back():
        """Go back to opening screen"""
        for widget in frame_entry.winfo_children():
            widget.destroy()
        for widget in window.winfo_children():
            widget.destroy()        
        opening_screen()
        
        
    back_button = tk.Button(master=window, text="Go Back", command=back)


    entry_temperature.grid(row=0, column=0, sticky="e")
    label_temp.grid(row=0, column=1, sticky="w")
    frame_entry.grid(row=0, column=0, padx=10)
    btn_convert.grid(row=0, column=1, pady=10)
    label_result.grid(row=0, column=2, padx=10)
    back_button.grid(row=1, column=0, padx=5, pady=5)

def kelvin_chosen():

    def k_to_c():
        """Convert the value for Fahrenheit to Celsius and insert the result into label_result"""
        kelvin = entry_temperature.get()
        celsius = float(kelvin) - 273.15
        label_result["text"] = f"{round(celsius,2)} \N{DEGREE CELSIUS}"

    frame_entry = tk.Frame(master=window)
    entry_temperature = tk.Entry(master=frame_entry, width=10)
    label_temp = tk.Label(master=frame_entry, text="K")
    btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=k_to_c)
    label_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

    def back():
        """Go back to opening screen"""
        for widget in frame_entry.winfo_children():
            widget.destroy()
        for widget in window.winfo_children():
            widget.destroy()        
        opening_screen()
        
        
    back_button = tk.Button(master=window, text="Go Back", command=back)


    entry_temperature.grid(row=0, column=0, sticky="e")
    label_temp.grid(row=0, column=1, sticky="w")
    frame_entry.grid(row=0, column=0, padx=10)
    btn_convert.grid(row=0, column=1, pady=10)
    label_result.grid(row=0, column=2, padx=10)
    back_button.grid(row=1, column=0, padx=5, pady=5)


window.mainloop()