from django.urls import path

from yculture import play
from .views import gamemanager_view

urlpatterns = [
    path('gamemanager/', gamemanager_view, name='gamemanager'),
]
