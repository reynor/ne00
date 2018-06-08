from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#添加内容
from datetime import datetime
from django.template import RequestContext
#from .forms import AccountForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #ajax
from master.models import Staff, Product, partUnit, Tag, Company
import json

#from .models import Staff, Product

@login_required
def products(request):
    return render(request, 'storepage.html')

def searchProduct(request):
    searchId = request.POST['searchId'].split(' ') 
    searchName = request.POST['searchName'].split(' ') 
    searchBrand = request.POST['searchBrand'].split(' ') 
    searchSpec = request.POST['searchSpec'].split(' ') 
    searchNote = request.POST['searchNote'].split(' ') 
    
    sql = "Product.objects.filter(productId__icontains='')"

    for a in searchId:
        if str(a) == '':
            pass
        else:
            sql = sql + ".filter(productId__icontains='"+str(a)+"')"
    for a in searchName:
        if str(a) == '':
            pass
        else:
            sql = sql + ".filter(productName__icontains='"+str(a)+"')"
    for a in searchBrand:
        if str(a) == '':
            pass
        else:
            sql = sql + ".filter(productBrand__icontains='"+str(a)+"')"
    for a in searchSpec:
        if str(a) == '':
            pass
        else:
            sql = sql + ".filter(specification__icontains='"+str(a)+"')"
    for a in searchNote:
        if str(a) == '':
            pass
        else:
            sql = sql + ".filter(note__icontains='"+str(a)+"')"
    
    products = eval(sql)    #执行动态python语句

    js = '['
    for a in products:
        js= js + str(a.toJSON()) + ','
    js = js[:-1]    #去掉最后一个字符
    js = js + ']'
    return HttpResponse(js)

def receipt(request):
    return render(request, 'receiptpage.html')