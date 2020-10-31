from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("process_money", views.process_money),
    path("reset", views.reset),
    path("gold_api", views.gold_api)
]
