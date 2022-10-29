from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def mainView(request):
    content = ProductsModel.objects.all()
    context = {
        "content": content
    }
    return render(request, "index.html", context=context)