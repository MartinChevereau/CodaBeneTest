from dataclasses import field
from pickle import FALSE
from random import choice
from django import forms
from .models import *


class ExpiriesForm(forms.Form):

    products = ProductsModel.objects.all()
    expiry_date = forms.DateField()
    choices = []
    for product in products:
        choices.append((product.GTIN, product.format()))
    GTIN = forms.ChoiceField(choices=choices)