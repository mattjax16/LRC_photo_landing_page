from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login', views.login_view, name='login'),
    path('index', views.index, name='index'),
    path('upload', views.upload_view, name='upload'),
    path('signup', views.signup_view, name='signup'),
]