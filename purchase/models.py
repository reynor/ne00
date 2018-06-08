from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import copy
import json
from master.models import Staff, Product, partUnit, Tag, Company
from projects.models import Mechine, Project

class Purchase(models.Model):    
    purchaseId = models.CharField(max_length=20, null=True, db_index=True)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    