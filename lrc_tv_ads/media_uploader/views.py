from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the media_uploader page!!!!")
# Create your views here.

def upload_view(request):
    return  HttpResponse("<h1>This is the call to bring up the uploader interface <h1>")

def login_view(request):
    return HttpResponse("This is the login page for the media_uploader.")

def signup_view(request):
    return  HttpResponse("<h1>This is the call to bring up the SIGNUP interface <h1>")

def home(response):
    pass