#web.py
#
from flask import Flask, render_template, request
from weather2 import get_location, get_weather



app = Flask(__name__)

@app.route("/")

def index():
	#define variables
	city_name = request.values.get('city')
	weather = get_weather(city_name)
	weathersum = weather[0].lower()
	weathertemp = weather[1]
	return render_template("index.html", city=city_name, weathersum=weathersum, weathertemp=weathertemp)

@app.route("/about")

def about():
	return render_template("about.html")

if __name__ == "__main__":
    app.run()
