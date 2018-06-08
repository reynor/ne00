from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#import django.contrib.auth.views
from datetime import datetime

urlpatterns = [
    path('store/',views.products,name='store'),
    path('searchProduct/',views.searchProduct,name='searchP'),
    path('receipt/',views.receipt,name='receiptP'),
]
