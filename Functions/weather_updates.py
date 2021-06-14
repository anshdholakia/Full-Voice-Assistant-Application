import requests #import these modulas
import json
import math

# referenced this code from https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
api_key = "2f01656a7c929d75580b90fc41511e50"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

CITY= input("Enter city name : ") 

Update_url = base_url + "appid=" + api_key + "&q=" + CITY
response = requests.get(Update_url) 
pythonformat = response.json() 


if pythonformat["cod"] != "404": 
	name = pythonformat["main"] 
	current_temperature = name["temp"] 
	current_humidiy = name["humidity"] 
	Desc = pythonformat["weather"] 
	weather_description = Desc[0]["description"] 

#math calcualtion for converting into fahreneit 
	cel = current_temperature - 273.15
	fah = cel * (9 / 5) + 32

	print(" Temperature (in Fahrenheit Units) = " + str(fah) +
	"\n Humidity =" + str(current_humidiy) +
	"\n Description = " + str(weather_description))

else: 
	print("Cannot find the location ") 
