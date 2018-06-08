from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import copy
import json
from master.models import Staff, Product, partUnit, Tag, Company
from projects.models import Mechine
from purchase.models import Purchase

class Receipt(models.Model):
    receiptId = models.CharField(max_length=20, unique=True, db_index=True)
    purchaseId = models.ForeignKey(Purchase, null=True, on_delete=models.SET_NULL)
    vendor = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    note = models.TextField(null=True)
    receipter = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    receiptTime = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    modiUser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)

class Outbound(models.Model):
    sender = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    sendTime = models.DateTimeField()
    makeFor = models.ForeignKey(Mechine, null=True, on_delete=models.SET_NULL)#用料机台号
    worker = models.CharField(max_length=20, null=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
    modiUser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class StoreItem(models.Model):
    receipt = models.ForeignKey(Receipt, related_name='Items', on_delete=models.CASCADE)
    out = models.ForeignKey(Outbound, related_name='Items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(partUnit, null=True, on_delete=models.SET_NULL)
    itemCount = models.FloatField()
    note = models.TextField(null=True)
    modified = models.DateTimeField(auto_now=True)
    modiUser = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product.productName + ":" + str(self.itemCount)
