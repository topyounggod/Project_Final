"""isagagae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
import mainblog.views

urlpatterns = [
    # path('', mainblog.views.index, name='index'),
    path('',include('mainblog.urls'),name= 'mainblog'),
    path('admin/', admin.site.urls),
    path('',include('star.urls')),
    # path('map/', mainblog.views.showmap, name='showmap'),
    # path('memotest/', mainblog.views.memotest, name = 'memotest'),
    # path('deleteMemo/', mainblog.views.doneMemo, name = 'deleteMemo'),
    # path('savestar/', mainblog.views.savestar, name = 'savestar'),
    # path('service/',mainblog.views.service,name ='service')
#    path('result/',mainblog.views.result,name='result')
]
