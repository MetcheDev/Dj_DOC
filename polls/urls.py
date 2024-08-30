from django.urls import path

from . import views


app_name = "polls"
urlpatterns = [
    path('', views.index, name="index"),#detail/2
    path('detail/<int:question_id>/', views.detail, name="detail" )#detail/2
    
]