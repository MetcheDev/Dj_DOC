from django.urls import path

from . import views


#/sample
urlpatterns = [
    path('', views.index, name="index"),#/sample
    path('sample/', views.sample)#/sample
]