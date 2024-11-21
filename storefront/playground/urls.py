from django.urls import path
from . import views

urlpatterns = [
  path("playground/hellow/", views.say_hel)
]
 
