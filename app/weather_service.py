import requests
from flask import current_app as app

def get_weather(city_name):
    API_KEY= app.config["OPENWEATHER_API_KEY"]
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return None

def get_icon_url(state):
    """
    img = None
    if state=='Clouds':
        img='clouds.png'
    elif state=='Drizzle':
        img='drizzle.png'
    elif state=='Rain':
        img='rain.png'
    elif state=='Snow':
        img='snow.png'
    elif state=='Clear':
        img='clear.png'
    elif state=='Mist':
        img='mist.png'
    """
    return f"https://openweathermap.org/img/wn/{state}@2x.png"
