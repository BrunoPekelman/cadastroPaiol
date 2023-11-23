from django.urls import path
from galeria.views import index, create, store

urlpatterns = [
    path('', index),
    path('create/', create),
    path('store/', store)
]