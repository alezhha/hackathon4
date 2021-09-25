from django.urls import path
from .views import main, send


urlpatterns = [
    path("", main ,name = "mainpage"),
    path('send/', send, name='send'),
]