from django.shortcuts import render
import requests

def index(request):
    appid = '0e3f0f3d420b4960e2d0eb6c637db1e7'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)
