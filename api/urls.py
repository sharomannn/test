from django.urls import path
from .views import hello_personalized, Authors
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('hello/', hello_personalized),
]

router = DefaultRouter()

router.register('authors', Authors, basename='authors')

urlpatterns += router.urls