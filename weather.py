from pyfiglet import Figlet
from gtts import gTTS as gt
import requests
import json
import os
f = Figlet(font='slant')
print (f.renderText('weather report'))
City = str(input('enter your city name: '))
api_key ='04018081b69cca6f721c5ed1a46be071'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
url = base_url+'appid='+api_key+'&q='+City+'&units=metric'
response = requests.get(url)
x=response.json()
if x['cod']!=401:
    print ('city name:',x['name'])
    print ('weather:',x['weather'])
    print ('weather:',x['weather'][0]['main'])
    print ('temp:',x['main']['temp'])
    print ('minimum temp:',x['main']['temp_min'])
    print ('max temp:',x['main']['temp_max'])
else:
    print ('city not found')
a = x['weather'][0]['main']
b = x['main']['temp']
c = x['main']['temp_min']
d = x['main']['temp_max']
weather_report=f'It mostly {a} today.Current temperature in {City} is {b}°Celsius.High of {c}°Celsius and low of {d}°Celsius .Thank u sir'
language = 'en'
output = gt(text = weather_report,lang = language)
output.save('weather.mp3')
os.system('mpv /data/data/com.termux/files/home/weather')
