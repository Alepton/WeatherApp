from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from django.views.generic import DeleteView, DetailView

class CityDalate(DeleteView):
    model = City
    success_url = '/'
    template_name = 'weather/city_delete.html'


def index(request):
    appid = '0e3f0f3d420b4960e2d0eb6c637db1e7'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    error = ''

    if request.method == 'POST':       # проверка того что форма отправлена методом POST
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Введены не корректные данные"

    form = CityForm()     # эта строка нужна для очиски формы после отправки

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'id': city.id,
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'wind': res["wind"]["speed"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form, 'error': error}

    return render(request, 'weather/index.html', context)
