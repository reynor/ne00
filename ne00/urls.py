"""ne00 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url
#自建内容
from master import views as master_view
from products import views as products_view
#from master import forms as master_forms
from datetime import datetime

urlpatterns = [
    path(r'',master_view.main),
    #path('login/',master_view.login,name='login'),
    path('home/',include('master.urls')),
    path('maindata/',include('products.urls')),
    path('projects/',include('projects.urls')),
    path('purchase/',include('purchase.urls')),
    path('store/',include('store.urls')),
    path('F95T/', admin.site.urls),
]
