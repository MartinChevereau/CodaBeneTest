from dataclasses import field
from pickle import FALSE
from random import choice
from django import forms
from .models import *


class ExpiriesForm(forms.Form):

    products = ProductsModel.objects.all()
    # the date format is the one expected by postgresql
    expiry_date = forms.DateField(input_formats=['%Y-%m-%d'])
    choices = []
    for product in products:
        choices.append((product.GTIN, product.format()))
    GTIN = forms.ChoiceField(choices=choices)