import tkinter as tk
import customtkinter
import tkinter.font as font

window = customtkinter.CTk()
window.geometry("300x100")
window.title("Age Calculator")
window.resizable(width=False, height=False)

def enterButton():
    year = year_entry.get()
    age = str(2022 - int(year))
    age_label.config(text=age)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

label_year = customtkinter.CTkLabel(master=window, text="Enter year of birth:", text_font=('Arial', 13))
label_year.place(relx=0.25, rely=0.2, anchor=tk.CENTER)

label_age = customtkinter.CTkLabel(master=window, text="Age:", text_font=('Arial', 13))
label_age.place(relx=0.42, rely=0.7, anchor=tk.CENTER)

year_entry = customtkinter.CTkEntry(master=window, width=50, height=10, placeholder_text="Year")
year_entry.place(relx=0.65, rely=0.2, anchor=tk.E)

enter_button = customtkinter.CTkButton(master=window, text="Enter", width=80, height=7, corner_radius=5, command=enterButton)
enter_button.place(relx=0.7, rely=0.10)

age_label = customtkinter.CTkLabel(master=window, text="", text_font=('Arial', 13), width=50)
age_label.place(relx=0.48, rely=0.55)


window.mainloop()