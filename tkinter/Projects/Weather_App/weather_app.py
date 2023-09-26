import sys
import tkinter as tk
from tkinter import font
import requests
from PIL import ImageTk, Image 
import time

window = tk.Tk()
window.geometry('750x500')
#window.resizable(width=False, height=False)

def opening():

	def format_response(weather):
		try:
			name = weather['city']['name']
			temperature_today = weather['list'][0]['main']['temp']
			desc = weather['list'][0]['weather'][0]['description']
			temp_feels = weather['list'][0]['main']['feels_like']
			humidity = weather['list'][0]['main']['humidity']
			wind_speed = weather['list'][0]['wind']['speed']

			final_str = f'City: {name} \nTemperature now: {temperature_today}°C --- feels like: {temp_feels}°C \nCondtions: {desc} \nHumidty: {humidity}% \nWind Speed: {wind_speed}m/s'

		except:
			final_str = 'There was a problem retrieving that information'

		return final_str

	def get_weather(city):

		weather_key = 'a9f553857df50650433c1577e3be6538'
		url = 'http://api.openweathermap.org/data/2.5/forecast'
		params = {'q': city, 'appid': weather_key, 'units': 'metric'}
		response = requests.get(url, params=params)
		weather = response.json()
		label_below['text'] = format_response(weather)

		temp_tmr = tk.Button(second_frame, font=('Bookman Old Style', 10), text="Tomorrow's Forecast", command=tomorrow)
		temp_tmr.place(relx=0.74, rely=0.88, relwidth=0.25, relheight=0.1)

	def resize_image(event):
		new_width = event.width
		new_height = event.height
		image = copy_of_image.resize((new_width, new_height))
		photo = ImageTk.PhotoImage(image)
		label.config(image = photo)
		label.image = photo


	image = Image.open('img\clouds.jpg')
	copy_of_image = image.copy()
	photo = ImageTk.PhotoImage(image)
	label = tk.Label(window, image = photo)
	label.bind('<Configure>', resize_image)
	label.pack(fill=tk.BOTH, expand = True)

	top_frame = tk.Frame(window, bg="#0cc961", bd=5)
	top_frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.15)

	city_entry = tk.Entry(top_frame, font=('Bookman Old Style', 22))
	city_entry.place(relwidth=0.65, relheight=1)

	enter_button = tk.Button(top_frame, font=('Bookman Old Style', 18), text="Enter", command=lambda: get_weather(city_entry.get()))
	enter_button.place(relx=0.68, relwidth=0.31, relheight=1)

	second_frame = tk.Frame(window, bg="#0cc961", bd=5)
	second_frame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.7)

	label_below = tk.Label(second_frame, font=('Bookman Old Style', 15), anchor="nw", justify="left", bd=4)
	label_below.place(relwidth=1, relheight=1)

	return second_frame, city_entry

opening()

second_frame, city_entry = opening()

def tomorrow():
	second_frame = tk.Frame(window, bg="#0cc961", bd=5)


	for widget in second_frame.winfo_children():
		widget.place_forget()

	def format_response2(weather):
		try:
			name2 = weather['city']['name']
			temperature_tmr = weather['list'][1]['main']['temp']
			desc_tmr = weather['list'][1]['weather'][0]['description']
			temp_feels_tmr = weather['list'][1]['main']['feels_like']
			humidity_tmr = weather['list'][1]['main']['humidity']
			wind_speed_tmr = weather['list'][1]['wind']['speed']

			final_str = f'City: {name2} \nTemperature tomorrow: {temperature_tmr}°C --- will feel like: {temp_feels_tmr}°C \nCondtions: {desc_tmr} \nHumidty: {humidity_tmr}% \nWind Speed: {wind_speed_tmr}m/s'
		except:
			final_str = 'There was a problem retrieving that information'

		return final_str


	def goback():
		for widget in second_frame.winfo_children():
			if isinstance(widget, tk.Label):
				widget["text"] = ""
			elif isinstance(widget, tk.Entry):
				widget.delete(0, 'end')

		opening()
	"""
	def goback():
		for widget in second_frame.winfo_children():
			widget.place_forget()
	
		opening()
	"""

	second_frame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.7)

	label_below2 = tk.Label(second_frame, font=('Bookman Old Style', 15), anchor="nw", justify="left", bd=4)
	label_below2.place(relwidth=1, relheight=1)

	temp_yest = tk.Button(second_frame, font=('Bookman Old Style', 10), justify="left", text="Go back", command=goback)
	temp_yest.place(relx=0.01, rely=0.88, relwidth=0.12, relheight=0.1)

	weather_key2 = 'a9f553857df50650433c1577e3be6538'
	url2 = 'http://api.openweathermap.org/data/2.5/forecast'
	params2 = {'q': city_entry.get(), 'appid': weather_key2, 'units': 'metric'}
	response2 = requests.get(url2, params=params2)
	weather2 = response2.json()
	label_below2['text'] = format_response2(weather2)
		
window.mainloop()