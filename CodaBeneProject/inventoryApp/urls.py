from django.urls import path
from . import views

urlpatterns = [
    path('addProduct', views.addProductView, name='mainView'),
    path('', views.checkExpiriesView, name='mainView'),
]
