from django.urls import path
from .views import hello_personalized

urlpatterns = [
    path('hello/', hello_personalized),
]
