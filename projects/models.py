from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import copy
import json
from master.models import Staff, Product, partUnit, Tag, Company

class Project(models.Model):
    product = models.ManyToManyField(Product)

class Mechine(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    mechineId = models.CharField(max_length=20, unique=True, db_index=True)
    