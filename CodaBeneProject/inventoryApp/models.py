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


class ProductsModels(models.Model):
    GTIN = models.IntegerField(primary_key=TRUE,
                               default=random.randint(0, 10**9 - 1))
    shelf = models.OneToOneField(ShelvesModel, on_delete=models.PROTECT)
    brand = models.CharField(max_length=256)
    flavor = models.CharField(max_length=256)


class ExpiriesModels(models.Model):
    id = models.AutoField(primary_key=TRUE)
    GTIN = models.OneToOneField(ProductsModels, on_delete=models.PROTECT)
    expiry_date = models.DateField()