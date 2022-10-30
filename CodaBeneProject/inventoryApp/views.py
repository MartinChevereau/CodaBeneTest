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
            data = request.POST
            # this allows us to update the expiry if the GTIN already exists
            product = ProductsModel.objects.get(GTIN=data["GTIN"])
            newExpiry, _ = ExpiriesModel.objects.get_or_create(GTIN=product)
            newExpiry.expiry_date = data["expiry_date"]
            newExpiry.save()

    context = {
        'form' : form,
        'submitted' : submitted,
        'valid' : valid
    }
    return render(request, "addProduct.html",context)

def checkExpiriesView(request):
    form = FilterShelvesFrom()
    # if we receive answer for the filter form we display accordingly
    if request.method == 'POST':
        data = request.POST
        # code to indicate that we take all shelves
        if data['shelf'] != '-1':
            expiries = ExpiriesModel.objects.filter(GTIN__shelf__id=data['shelf'] ).order_by('expiry_date')
        else:
            expiries = ExpiriesModel.objects.all().order_by('expiry_date')
    # if this is the first time we get the page we display all
    else:
        expiries = ExpiriesModel.objects.all().order_by('expiry_date')



    context = {
        "content" : expiries,
        "form": form
    }
    return render(request, "checkExpiries.html", context)