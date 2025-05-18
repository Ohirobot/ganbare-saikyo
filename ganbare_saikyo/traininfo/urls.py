from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_mock_data, name='index'),  # トップページ
    path('about/', views.about, name='about'),     # Aboutページ
    path('load-mock/', views.load_mock_data, name='load_mock'),  # デバッグ用
]
