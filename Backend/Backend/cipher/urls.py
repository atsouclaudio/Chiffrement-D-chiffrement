from django.urls import path
from .views import cipher_api

urlpatterns = [
    path("", cipher_api),  # l’endpoint sera /api/cipher/
]
