# https://flask.palletsprojects.com/en/1.1.x/quickstart/

# to get a free template go to https://html5up.net/  and download one. 
# in Chrome - open up Chrome developer tools, go to Console, and type some javascript - document.body.contentEditable=true
# after editing the html, save as to get teh html code locally. 
# to get great images for background use unsplash.com
import requests

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/weather')
def getweather():
    response = requests.get('http://weatherapp-weather-1:5001/weather')
    weather = response.json()
    description = weather["description"]
    icon = weather["icon"]
    icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
    return render_template("showweather.html", description=description, icon_url=icon_url)

if __name__ == "__main__":
    #app.run()
    app.run(debug=True)



