from email import message
from multiprocessing import context
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def addProductView(request):
    form = ExpiriesForm()
    submitted = False
    valid = False
    if request.method == 'POST':
        submitted = True
        # checking if date input is valid
        form = ExpiriesForm(request.POST)
        if form.is_valid():
            valid = True

    context = {
        'form' : form,
        'submitted' : submitted,
        'valid' : valid
    }
    return render(request, "addProduct.html",context)