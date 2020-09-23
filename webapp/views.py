from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return HttpResponse("<h2>Welcome to my first Web Portal!</h2>")
