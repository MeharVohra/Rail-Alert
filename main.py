# An API(Application Programming Interface) is a set of
# commands, functions, protocols or objects that programmers
# can use to create software or interact with an external system

import requests
from twilio.rest import Client
my_lat = 28.669081
my_lon = 77.430412

# Your API key
my_apikey = "ba63ce10f501f6abe0061a09cf86ceac"
# Parameters that we have to give while making a request to the endpoint url
parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": my_apikey,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# Raise an error message if there is one
response.raise_for_status()

account_sid = "ACc67b5a8d71b3349f6151a22e71a6ce85"
auth_token = "594fc2ec5b0906101b42f4b99a23d48b"

weather_data = response.json()
print(weather_data)
will_rain = False
# We need the next 12 hours of data and their respective ids
for positions in range(0, 12):
    weather_id = weather_data["hourly"][positions]["weather"][0]["id"]

# Setting the conditions for rain
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
         body="It's going to rain today 🌧 .Don't forget to carry your ☂ ",
         from_="+16788317364",
         to='+917042182525'
               )
    print(message.status)

elif not will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
         body="It's going to be a clear weather today 🌥. Have a nice day!",
         from_="+16788317364",
         to='+917042182525'
               )
    print(message.status)


# Finally use PYTHON ANYWHERE to schedule this task everyday.
