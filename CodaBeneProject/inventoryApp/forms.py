from dataclasses import field
from pickle import FALSE
from random import choice
from django import forms
from .models import *


class ExpiriesForm(forms.Form):

    products = ProductsModel.objects.all()
    # the date format is the one expected by postgresql
    expiry_date = forms.DateField(input_formats=['%Y-%m-%d'], help_text='format : YYYY-MM-DD')
    choices = []
    for product in products:
        choices.append((product.GTIN, product.format()))
    GTIN = forms.ChoiceField(choices=choices)

class FilterShelvesFrom(forms.Form):
    shelves = ShelvesModel.objects.all()
    choices = [(-1, "all")]
    for shelf in shelves:
        choices.append((shelf.id, shelf.name))
    shelf = forms.ChoiceField(choices=choices)