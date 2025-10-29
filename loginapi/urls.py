from django.urls import path
from .views import RegisterAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('register/', RegisterAPI.as_view(), name='register'),
]
