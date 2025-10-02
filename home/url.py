from django.urls import path 
from . import views


urlpatterns = [
    path('' ,views.home_sec, name='home'),
]