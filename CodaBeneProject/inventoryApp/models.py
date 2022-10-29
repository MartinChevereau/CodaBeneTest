from email.policy import default
from pickle import TRUE
import random
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class ShelvesModel(models.Model):
    id = models.AutoField(primary_key=TRUE)
    name = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name

def random_GTIN():
    return random.randint(0, 10**8 - 1)
class ProductsModel(models.Model):
    GTIN = models.IntegerField(primary_key=TRUE,
                               default=random_GTIN)
    shelf = models.ForeignKey(ShelvesModel, on_delete=models.PROTECT)
    brand = models.CharField(max_length=256)
    flavor = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='', unique=TRUE, null=TRUE)
    def __str__(self) -> str:
        return f"{self.shelf} of brand : {self.brand} and flavor: {self.flavor}"

class ExpiriesModel(models.Model):
    id = models.AutoField(primary_key=TRUE)
    GTIN = models.ForeignKey(ProductsModel, on_delete=models.PROTECT)
    expiry_date = models.DateField(null=TRUE)
    def __str__(self) -> str:
        return f"{self.GTIN} expiring : {self.expiry_date}"
