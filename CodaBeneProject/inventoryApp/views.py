from email import message
from multiprocessing import context
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def addProductView(request):
    form = ExpiriesForm()
    if request.method == 'POST':
        form = ExpiriesForm(request.POST)
        submitted = TRUE
    else:
        submitted = FALSE

    context = {
        'message' : message,
        'submitted' : submitted
    }
    return render(request, "addProduct.html",context)