from flask import Blueprint, render_template, request
from .weather_service import get_weather,get_icon_url

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    icon_url = None

    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)
        weather_data["main"]["temp"]=round(weather_data["main"]["temp"])
        icon_url = get_icon_url(weather_data["weather"][0]["icon"])
        print(icon_url)

    return render_template("index.html", weather=weather_data, icon_url=icon_url)
