from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addProduct_view(request):
    return HttpResponse("<h1> Add product</h1>")