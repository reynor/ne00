from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#添加内容
from datetime import datetime
from django.template import RequestContext
#from .forms import AccountForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #ajax
import json
from master.models import Staff, Product, partUnit, Tag, Company

#from .models import Staff, Product

@login_required
def products(request):
    return render(request, 'productpage.html')

@login_required
def addProduct(request):
    productId = request.POST['productId']
    productName = request.POST['productName']
    specification = request.POST['specification']
    productBrand = request.POST['productBrand']
    note = request.POST['note']
    if request.POST['id'] == '0':
        Product.objects.create(productId=productId, productName=productName,specification=specification,productBrand=productBrand,note=note)
        return HttpResponse('finish')
    else:
        pass
        # twz = partUnit.objects.get(id=request.POST['edid'])
        # twz.dimension = dimension
        # twz.conversion = conversion
        # twz.save()  # 最后不要忘了保存！！！
        # return HttpResponse(request.POST['edid'])
        # # return HttpResponse(product.__str__())
