import requests

#twilio api allows for sending text messages for a trial amount
from twilio.rest import Client

MY_LAT = "33.836594"
MY_LONG = "-117.914299"
# text account info
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

# getting the weather info from openweathermap
API_KEY = API
weather_api_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "imperial",

}
response = requests.get(weather_api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_it_rain = False
# check weather codes for rain in the next 6 hours
for x in range(0, 2):
    weather_code = weather_data["list"][x]["weather"][0]["id"]
    if weather_code < 700:
        will_it_rain = True

# if it will rain it will send a next to bring an unmbrella
if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain in the next 6 hours make sure to bring an umbrella ☂️",
        from_='+18449632136',
        to='+19495665873'
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="No rain, in the next 6 hours",
        from_='+18449632136',
        to='MY NUMBER'
    )
