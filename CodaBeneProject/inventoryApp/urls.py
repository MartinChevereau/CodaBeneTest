from django.urls import path
from . import views

urlpatterns = [
    path('', views.addProduct_view, name='addProduct_view'),
]
