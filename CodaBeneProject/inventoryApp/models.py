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
        return f"{str(self.shelf)[:-1]} of brand : {self.brand} and flavor: {self.flavor}"
    
    # prettier printing to display GITN
    def format(self):
        return f"{self.GTIN:08d} / {self}"

class ExpiriesModel(models.Model):
    GTIN = models.OneToOneField(ProductsModel, on_delete=models.PROTECT, unique=TRUE, primary_key=TRUE)
    expiry_date = models.DateField(null=TRUE)
    def __str__(self) -> str:
        return f"{self.GTIN} expiring : {self.expiry_date}"
