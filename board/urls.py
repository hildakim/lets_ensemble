from django.contrib import admin
from django.urls import path
from .views import *

app_name = "board"

urlpatterns = [
    path('', home, name="home"),
    path('post/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('edit/<str:id>', edit, name="edit"),
    path('delete/<str:id>', delete, name="delete"),
    path('sendmail/', sendmail, name="sendmail"),
]