from django.urls import path

from cabinet import views

app_name = 'cabinet'
urlpatterns = [
    path('', views.index, name='index'),
]
