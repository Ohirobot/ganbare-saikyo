from django.urls import path
from . import views

app_name= 'saikyodelay'
urlpatterns = [
    path('', views.show_delayinfo, name='show_delayinfo'),
]