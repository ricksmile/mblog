"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mainsite.views import homepage, showpost,about,listing,disp_detail

urlpatterns = [
    url(r'^$', homepage),
    url(r'^post/(\w+)$', showpost),
    url(r'^about/', about),
	url(r'^list/([0-9a-zA-Z]+)/$',disp_detail),
    url(r'^list/$', listing),
    url(r'^admin/', include(admin.site.urls)), 
]
