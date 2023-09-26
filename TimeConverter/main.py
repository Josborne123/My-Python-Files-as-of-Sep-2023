import tkinter as tk
import customtkinter
import time
import pytz
from pytz import timezone
from datetime import datetime
from tkinter import font

# Main Program
window = customtkinter.CTk()
window.geometry('700x600')
window.title("Time Converter")
window.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")


def clock():
    currentTime = time.strftime("%H:%M:%S")
    systemZone = time.strftime("%Z")
    systemTimeInfo = f"{currentTime} - {systemZone}"
    systemTime = customtkinter.CTkLabel(clockFrame, text=systemTimeInfo, font=("Courier New Bold", 24))
    systemTime.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
 

    ct = timezone('US/Central')
    cet = datetime.now(ct)
    cetTime = (cet.strftime("%H:%M"))
    cetOutput = f"Central Time - {cetTime}"
    ctLabel = customtkinter.CTkLabel(timezoneFrame, text=cetOutput, font=("Courier New Bold", 15))
    ctLabel.place(relx=0.05, rely=0.05)

    et = timezone('US/Eastern')
    est = datetime.now(et)
    estTime = (est.strftime("%H:%M"))
    estOutput = f"Eastern Time - {estTime}"
    etLabel = customtkinter.CTkLabel(timezoneFrame, text=estOutput, font=("Courier New Bold", 15))
    etLabel.place(relx=0.6, rely=0.05)

    pt = timezone('US/Pacific')
    pet = datetime.now(pt)
    petTime = (pet.strftime("%H:%M"))
    petOutput = f"Pacific Time - {petTime}"
    ptLabel = customtkinter.CTkLabel(timezoneFrame, text=petOutput, font=("Courier New Bold", 15))
    ptLabel.place(relx=0.05, rely=0.17)

    mt = timezone('US/Mountain')
    met = datetime.now(mt)
    metTime = (met.strftime("%H:%M"))
    metOutput = f"Mountain Time - {metTime}"
    mtLabel = customtkinter.CTkLabel(timezoneFrame, text=metOutput, font=("Courier New Bold", 15))
    mtLabel.place(relx=0.6, rely=0.17) 
    
    window.after(1000, clock)

def processData():
    # Clearing the Frame
    for widget in outputFrame.winfo_children():
        widget.place_forget()

    #hourTimeInput.delete(0, 'end')
    #minuteTimeInput.delete(0, 'end')
    
    location = dropDown.get()
    userLocationLabel = customtkinter.CTkLabel(outputFrame, text=location, font=("Courier New Bold", 40))
    userLocationLabel.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    hourUserTime = hourTimeInput.get()
    minuteUserTime = minuteTimeInput.get()
    hourUserTime = hourUserTime[0:2]
    minuteUserTime = minuteUserTime[0:2]
    userTime = f"{hourUserTime}:{minuteUserTime}" 
    print(userTime)

page1Frame = customtkinter.CTkFrame(window, fg_color="transparent")
page2Frame = customtkinter.CTkFrame(window, fg_color="transparent")

page1Frame.place(relwidth=1, relheight=1)
page2Frame.place(relwidth=1, relheight=1)


# Page 1
clockFrame = customtkinter.CTkFrame(page1Frame, fg_color="transparent")
clockFrame.place(relx=0.225, rely=0.1, relwidth=0.55, relheight=0.06)

timezoneFrame = customtkinter.CTkFrame(page1Frame)
timezoneFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)

currentTimeButton = customtkinter.CTkButton(page1Frame, text="Current", font=("Courier New Bold", 15), width=12, command=lambda: page1Frame.tkraise())
currentTimeButton.place(relx=0.01, rely=0.01)

chooseTimeButton = customtkinter.CTkButton(page1Frame, text="Choose Time", font=("Courier New Bold", 15), width=14, command=lambda: page2Frame.tkraise())
chooseTimeButton.place(relx=0.135, rely=0.01)


# Page 2
inputFrame = customtkinter.CTkFrame(page2Frame)
inputFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.18)

outputFrame = customtkinter.CTkFrame(page2Frame)
outputFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

currentTimeButton2 = customtkinter.CTkButton(page2Frame, text="Current", font=("Courier New Bold", 15), width=12, command=lambda: page1Frame.tkraise())
currentTimeButton2.place(relx=0.01, rely=0.01)

chooseTimeButton2 = customtkinter.CTkButton(page2Frame, text="Choose Time", font=("Courier New Bold", 15), width=14, command=lambda: page2Frame.tkraise())
chooseTimeButton2.place(relx=0.135, rely=0.01)

locationLabel = customtkinter.CTkLabel(inputFrame, text="Location:", font=("Courier New Bold", 15))
locationLabel.place(relx=0.01, rely=0.1, relwidth=0.25)

dropDown = customtkinter.CTkOptionMenu(inputFrame, values=["Japan", "Canada", "US/Eastern", "US/Western"], anchor="w")
dropDown.place(relx=0.285,rely=0.1)

timeLabel = customtkinter.CTkLabel(inputFrame, text="Time:", font=("Courier New Bold", 15))
timeLabel.place(relx=0.01, rely=0.6, relwidth=0.25)

hourTimeInput = customtkinter.CTkEntry(inputFrame, width=30)
hourTimeInput.place(relx=0.21, rely=0.6)

colonLabel = customtkinter.CTkLabel(inputFrame, width=10, text=":", font=("Courier New Bold", 20))
colonLabel.place(relx=0.3, rely=0.6)

minuteTimeInput = customtkinter.CTkEntry(inputFrame, width=30)
minuteTimeInput.place(relx=0.34, rely=0.6)



hourTimeInput.bind("<Return>", (lambda event: processData()))
minuteTimeInput.bind("<Return>", (lambda event: processData()))



print(pytz.all_timezones)



page1Frame.tkraise()
clock()
window.mainloop()