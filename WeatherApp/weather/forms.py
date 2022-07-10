from .models import City
from django.forms import ModelForm, widgets, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City            #привязка формы к модели City
        fields = ["name"]       # поле, которое будет у формы
        widgets = {"name": TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}
