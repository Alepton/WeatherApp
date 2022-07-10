from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>', views.CityDalate.as_view(), name='city_delete')
]
