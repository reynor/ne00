from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# 添加内容
from datetime import datetime
from django.template import RequestContext
from .forms import AccountForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # ajax
import json

from .models import Staff, Product, partUnit

# Create your views here.
'''
from django.views.generic.base import View
from django.template import loader
class SearchSubmitView(View): 
    template = 'search_submit.html'
    response_message = 'This is the response'
    
    def post(self, request): 
        template = loader.get_template(self.template) 
        query = request.POST.get('search', '') 
        # A simple query for Item objects whose title contain 'query' 
        items = Product.objects.all()
        context = {'title': self.response_message, 'query': query, 'items': items} 
        rendered_template = template.render(context, request) 
        return HttpResponse(rendered_template, content_type='text/html')
'''


@login_required
def getProducts(request):
    '''测试项，工作正常
    a = request.POST['a']
    b = request.POST['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))  
    '''
    products = Product.objects.values()
    products = list(products)
    for a in products:
        a['modified'] = a['modified'].strftime("%Y-%m-%d %H-%M-%S")
        # a['id']=str(a['id'])
    js = '{"data":'+json.dumps(products)+"}"
    return HttpResponse(js)
    '''实时数据反馈
    a = request.POST['a']
    return HttpResponse(str(a)+" -ajax")
    '''


@login_required
def getBom(request):
    partId = request.POST['id']
    product = Product.objects.get(pk=partId)
    products = product.Bom.all()
    c = []
    for a in products:
        # b=a.parentProduct
        b = a.product
        a.modified = a.modified.strftime("%Y-%m-%d %H-%M-%S")
        d = {'id': a.id, 'productId': b.productId, 'productName': b.productName, 'productBrand': b.productBrand,
             'specification': b.specification, 'unit': a.unit, 'itemCount': a.itemCount, 'modified': a.modified}
        c.append(d)
        # a['id']=str(a['id'])
    js = json.dumps(c)
    return HttpResponse(js)
    # return HttpResponse(product.__str__())


def login(request):
    return render(request, 'login.html')
    '''
    if request.method == 'POST':
        return HttpResponse(u"提交成功")
        form = AccountForm(request.POST)
        return HttpResponse(request.POST)
    '''


@login_required
def main(request):
    return render(request, 'homepage.html')


@login_required
def account(request):
    return render(request, 'account.html')


@login_required
def unit(request):
    return render(request, 'unitpage.html')


@login_required
def getunit(request):
    units = partUnit.objects.values()
    products = list(units)
    js = '{"data":'+json.dumps(products)+"}"
    return HttpResponse(js)


@login_required
def addunit(request):
    dimension = request.POST['dimension']
    conversion = request.POST['conversion']
    if request.POST['edid'] == '0':
        partUnit.objects.create(dimension=dimension, conversion=conversion)
        js = partUnit.objects.all()
        return HttpResponse(js)
    else:
        twz = partUnit.objects.get(id=request.POST['edid'])
        twz.dimension = dimension
        twz.conversion = conversion
        twz.save()  # 最后不要忘了保存！！！
        return HttpResponse(request.POST['edid'])
        # return HttpResponse(product.__str__())


@login_required
def delunit(request):
    delid = json.loads(request.POST['ids'])
    sql = "partUnit.objects"

    for a in delid:
        sql = sql + ".filter(id='" + str(a) + "')"
    sql = sql + '.delete()'
    try:
        exec(sql)
        return HttpResponse('succdss')
    except:
        print('faile')
