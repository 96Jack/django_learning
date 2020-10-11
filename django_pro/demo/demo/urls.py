"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from demo import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #
    url(r'^index/', views.index),
    #主路由调用子路由，用include方法
    url(r'^app/', include("App.urls")),
    url(r'^four/', include('four.urls')),
    url(r'^two/', include('two.urls')),

]
