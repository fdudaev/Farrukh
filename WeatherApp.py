import tkinter as tk
from tkinter import font
import requests

# from PIL import Image, ImageTk
# import os
HEIGHT = 500
WIDTH = 600


#
# ?q={city name},{state},{country code}&appid={your api key}
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature(°F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '470dd80c21d851234d816125c6beb754'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'AppID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)


def test_func(entry):
    print("Entry is : ", entry)


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='OT.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#99ceff", bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

search = tk.Button(frame, text="Search", bg="black", font=('Courier', 10), command=lambda: get_weather(entry.get()), fg='red')
search.place(relx=0.7, relheight=1, relwidth=0.3, )

lower_frame = tk.Frame(root, bg="#99ceff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


# print(tk.font.families())
root.mainloop()
