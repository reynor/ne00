from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#添加内容
from datetime import datetime
from django.template import RequestContext
from .forms import AccountForm

from .models import Staff

# Create your views here.


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
