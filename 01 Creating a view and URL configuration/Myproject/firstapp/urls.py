from django.urls import path
from . import views

urlpatterns = [
    path('message', views.home, name="home"),
]