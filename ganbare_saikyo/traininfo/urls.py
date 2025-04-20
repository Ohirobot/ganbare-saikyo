from django.urls import path
from . import views

urlpatterns = [
    path('api/status/saikyo', views.saikyo_status, name='saikyo_status'),
]
