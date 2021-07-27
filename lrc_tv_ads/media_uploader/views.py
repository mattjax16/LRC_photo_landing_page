from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the media_uploader page.")
# Create your views here.

def upload_view(request):
    return  HttpResponse("This is the call to bring up the uploader interface")