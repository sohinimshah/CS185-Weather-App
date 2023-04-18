from flask import Flask, render_template, jsonify, request
from pushbullet import Pushbullet
import config
import openai
import aiapi
import requests

def get_weather(weather_id):
    make_request = "https://api.weather.gov/stations/" + weather_id + "/observations/latest"

    # Make a GET request to the NWS API for the latest weather observations from the Boston Logan International Airport weather station (KBOS)
    response = requests.get(make_request)
    if response.status_code == 200:
        # Convert the response data to a Python dictionary
        data = response.json()
   
        # Extract the current temperature and weather condition from the response data
        current_temp = data['properties']['temperature']['value'] * (9/5) + 32
        current_condition = data['properties']['textDescription']
   
    #     # Print the current weather information
    #     print(f"The current temperature in {weather_id} is {current_temp: .1f} degrees Fahrenheit with {current_condition}.")
    # else:
    #     print("Error fetching data from API.")
    
    weather_info = "The current temperature in Dhaka is" + str(current_temp) + "degrees Fahrenheit and the conditions are" + current_condition
    return weather_info

def weather_to_chatGPT(weather_info):
    response_string = aiapi.generateChatResponse(weather_info)
    return response_string

def sendPush(message): 
    API_KEY = 'o.xWZrYH1njUqxI8TLKN37krUU3nwk53Hq'
    pb = Pushbullet(API_KEY)
    push = pb.push_note('Your Daily Weather Notification: ', message)

weather_data = get_weather("TJPS")
chatGPT_reccomendations = weather_to_chatGPT(weather_data)
sendPush(chatGPT_reccomendations)
# print(chatGPT_reccomendations)
