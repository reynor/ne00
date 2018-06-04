from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#添加内容
from datetime import datetime
from django.template import RequestContext
#from .forms import AccountForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #ajax
import json

#from .models import Staff, Product

@login_required
def products(request):
    return render(request, 'productpage.html')
