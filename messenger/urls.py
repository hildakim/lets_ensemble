from django.contrib import admin
from django.urls import path
from .views import *

app_name = "messenger"

urlpatterns = [
    path('', home, name="home"),
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
]