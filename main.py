from Ringo import begin

begin()
import time

try:
  import urequests as requests
except:
  import requests
  
try:
  import ujson as json
except:
  import json

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'enter ssid'
password = 'enter password'

city = 'London'
country_code = 'GB'


open_weather_map_api_key = 'enter api key'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

display.text('Connection successful')
display.fill(Display.Color.Gray)
display.text(str(station.ifconfig()), int(0), int(0), 0)

#set your unique OpenWeatherMap.org URL
open_weather_map_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country_code + '&APPID=' + open_weather_map_api_key

weather_data = requests.get(open_weather_map_url)
display.fill(Display.Color.Gray)
display.text(str(weather_data.json()))
time.sleep(1)
# Location (City and Country code)
display.fill(Display.Color.Gray)
location = 'Location: ' + weather_data.json().get('name') + ' - ' + weather_data.json().get('sys').get('country')
display.text(str(location), int(0), int(0), 0)

# Weather Description
description = 'Description: ' + weather_data.json().get('weather')[0].get('main')
display.text(str(description), int(50), int(0), 0)

# Temperature
raw_temperature = weather_data.json().get('main').get('temp')-273.15

# Temperature in Celsius
temperature = 'Temperature: ' + str(raw_temperature) + '*C'
#uncomment for temperature in Fahrenheit
#temperature = 'Temperature: ' + str(raw_temperature*(9/5.0)+32) + '*F'
display.text(str(temperature), int(100), int(0), 0)

def click1():
    global screenno,character,playerx,playery
    display.fill(Display.Color.Gray)
    pressure = 'Pressure: ' + str(weather_data.json().get('main').get('pressure')) + 'hPa'
    display.text(str(pressure), int(100), int(0), 0)

      
      

buttons.on_press(Buttons.Num_1, click1)

def click2():
    global screenno,character,playerx,playery
    display.fill(Display.Color.Gray)
    
    humidity = 'Humidity: ' + str(weather_data.json().get('main').get('humidity')) + '%'
    display.text(str(humidity), int(100), int(0), 0)
buttons.on_press(Buttons.Num_2, click2)

def click3():
    global screenno,character,playerx,playery
    display.fill(Display.Color.Gray)
    wind = 'Wind: ' + str(weather_data.json().get('wind').get('speed')) + 'mps ' + str(weather_data.json().get('wind').get('deg')) + '*'
    display.text(str(wind), int(100), int(0), 0)
    

buttons.on_press(Buttons.Num_3, click3)
