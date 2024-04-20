from django.contrib import admin
from django.urls import path, include

from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('registration', views.registration_view, name='registration'),
]
