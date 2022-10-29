from django.contrib import admin
from .models import ShelvesModel, ProductsModel

# Register your models here.
admin.site.register(ShelvesModel,)
admin.site.register(ProductsModel,)