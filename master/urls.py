from django.urls import path
from . import views

import django.contrib.auth.views
from datetime import datetime

urlpatterns = [
    path('',views.account,name='account'),
    path('login/',
        django.contrib.auth.views.login,
        {
            'template_name': 'login.html',
            #'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': '请登录',
                'year': datetime.now().year,
            }
        },
        name='login'),
    path('logout/',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    path('getdata/',views.getProducts,name='getdata'),
    path('getBom/',views.getBom,name='getBom'),
    path('unit/',views.unit,name='unit'),
    path('getunit/',views.getunit,name='getunit'),
    path('addunit/',views.addunit,name='addunit'),
    path('delunit/',views.delunit,name='delunit'),
]
