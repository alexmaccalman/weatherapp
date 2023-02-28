import requests
import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/weather')
def get_weather_from_omw():
    OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
    MY_LAT = 39.56633021926093 # Your latitude
    MY_LONG = -76.33500179850502 # Your longitude

    # read in environmental variables 
    api_key = os.getenv("API_KEY")
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")

    TEST_LAT = 42.112894
    TEST_LONG = -70.796805

    weather_params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": api_key,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()

    will_rain = False

    weather_slice = weather_data["hourly"][:1]
    condition_code = {}

    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]
        
    return condition_code

if __name__ == "__main__":
    #app.run()
    app.run(debug=True, port=5001)



