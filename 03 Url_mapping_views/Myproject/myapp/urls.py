from django.urls import path
from .import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path('menu/', views.Menu, name="Menu"),
    path("aboutus/", views.About, name="About"),
    path("book/", views.Book, name="Book"),
]