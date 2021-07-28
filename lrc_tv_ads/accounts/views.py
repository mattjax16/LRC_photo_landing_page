from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse


#imports for user actions and authentication
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


#check to see if user is authenticated or not
@login_required
def index(request):
    return render(request,'accounts/index.html')

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'accounts/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)


def home(response):
    pass