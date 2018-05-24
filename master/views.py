from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#添加内容
from datetime import datetime
from django.template import RequestContext
from .forms import AccountForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #ajax
import json

from .models import Staff, Product

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
    #js = '{"data":[["TP640-441","1","H300-015-100","新亿星","11-32"],["TP640-441","2","H300-015-100","新亿星","11-32"],["TP640-441","3","H300-015-100","新亿星","11-32"],["TP640-441","4","H300-015-100","新亿星","11-32"],["TP640-441","5","H300-015-100","新亿星","11-32"],["TP640-441","6","H300-015-100","新亿星","11-32"],["TP640-441","7","H300-015-100","新亿星","11-32"],["TP640-441","8","H300-015-100","新亿星","11-32"],["TP640-441","9","H300-015-100","新亿星","11-32"],["TP640-441","11","H300-015-100","新亿星","11-32"],["TP640-441","22","H300-015-100","新亿星","11-32"],["TP640-441","33","H300-015-100","新亿星","11-32"],["TP640-441","44","H300-015-100","新亿星","11-32"],["TP640-441","55","H300-015-100","新亿星","11-32"],["TP640-441","66","H300-015-100","新亿星","11-32"]]}'
    products=Product.objects.values()
    products=list(products)
    for a in products:
        a['modified']=a['modified'].strftime("%Y-%m-%d %H-%M-%S")
    js = '{"data":'+json.dumps(products)+"}"
    return HttpResponse(js)
    '''实时数据反馈
    a = request.POST['a']
    return HttpResponse(str(a)+" -ajax")
    '''

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
