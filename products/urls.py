from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#import django.contrib.auth.views
from datetime import datetime

urlpatterns = [
    path('products/',views.products,name='products'),
    path('addProduct/',views.addProduct,name='addProduct'),
    path('delproduct/',views.delproduct,name='delproduct'),
    path('postproductlist/',views.addProductList,name='addProductList'),
]
