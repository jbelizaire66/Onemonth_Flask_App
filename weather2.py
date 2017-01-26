# -*- coding: utf-8 -*-

#weather.py
# Based on Forecast.io

# my KEY: b754918b4564d3c6825e802be514e5f8
# APIs coming > Weather, Yelp, Slack (for bots)
# most API have been wrapped in languages like Python
# Do a search for forecast.io python, etc. and you'll find the wrapper.
# https://darksky.net/dev/register
# pwd: FB is the one bag

import forecastio
from geopy.geocoders import Nominatim
import os


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


#define a get_locaiton function. It returns a locaiton object
def get_location(address):
	geolocator = Nominatim()
	location = geolocator.geocode (address)
	return location

#define get_weather function that uses get_location sub-function
def get_weather(address):
	api_key = os.environ['FORECASTIO_API_KEY']
	location = get_location(address) 
	forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
	weather = []
	weather.append(forecast.summary)
	weather.append(forecast.temperature)
	return weather
