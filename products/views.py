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
from django.db.models import Q
from django.contrib.auth.decorators import permission_required

#from .models import Staff, Product

@login_required
def products(request):
    return render(request, 'productpage.html')

@login_required
@permission_required('master.add_product')
def addProduct(request):
    productId = request.POST['productId']
    productName = request.POST['productName']
    specification = request.POST['specification']
    productBrand = request.POST['productBrand']
    note = request.POST['note']
    if request.POST['id'] == '0':
        Product.objects.create(productId=productId, productName=productName,specification=specification,productBrand=productBrand,note=note)
        return HttpResponse('添加成功：'+productId+'  '+productName)
    else:
        temp = Product.objects.get(id=request.POST['id'])
        temp.productId = productId
        temp.productName = productName
        temp.specification = specification
        temp.productBrand = productBrand
        temp.note = note
        temp.save()
        return HttpResponse('修改成功：'+productId+'  '+productName)
        # twz = partUnit.objects.get(id=request.POST['edid'])
        # twz.dimension = dimension
        # twz.conversion = conversion
        # twz.save()  # 最后不要忘了保存！！！
        # return HttpResponse(request.POST['edid'])
        # # return HttpResponse(product.__str__())

@login_required
def delproduct(request):
    delid = json.loads(request.POST['ids'])
    print(delid)
    sql = "Product.objects.filter("

    i = True
    for a in delid:
        if i == True:
            sql = sql + "Q(id='" + str(a) + "')"
            i = False
        else:
            sql = sql + "|Q(id='" + str(a) + "')"
    sql = sql + ').delete()'
    try:
        exec(sql)
        return HttpResponse(sql)
    except:
        print('faile')

@login_required
def addProductList(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')

        import openpyxl
        wb=openpyxl.load_workbook(file_obj)  #打开excel文件
        print(wb.get_sheet_names())  #获取工作簿所有工作表名

        sheet=wb.get_sheet_by_name('Sheet1')  #获取工作表
        print(sheet.title) 

        sheet02=wb.get_active_sheet()  #获取活动的工作表
        print(sheet02.title) 

        return HttpResponse(wb.get_sheet_names())
    # return HttpResponse(product.__str__())