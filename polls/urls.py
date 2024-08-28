from django.urls import path

from . import views


#/polls/34/
urlpatterns = [
    path('', views.index, name="index"),#MATCH
    
]