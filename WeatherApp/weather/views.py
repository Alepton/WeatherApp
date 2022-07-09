from django.shortcuts import render
import requests
from .models import City

def index(request):
    appid = '0e3f0f3d420b4960e2d0eb6c637db1e7'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'wind': res["wind"]["speed"]
        }
        all_cities.append(city_info)

    context = {'info': all_cities}

    return render(request, 'weather/index.html', context)
