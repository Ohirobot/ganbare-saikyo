from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # トップページ
    path("about/", views.about, name="about"),  # Aboutページ
    path("load-mock/", views.load_mock_data, name="load_mock"),  # デバッグ用
    path(
        "api/train-status/", views.train_status_api, name="train_status_api"
    ),  # APIエンドポイント（JSに叩かせる）
]
