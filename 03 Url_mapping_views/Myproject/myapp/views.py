from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("<h1>Welcome to Little Lemon!</h1>")
def Menu(request):
    return HttpResponse("<h1>Menu for Little Lemon</h1>")
def About(request):
    return HttpResponse("<h1>About us</h1><br>We are ...")
def Book(request):
    return HttpResponse("Make a booking")
