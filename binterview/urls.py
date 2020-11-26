from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from tracking import views
from rest_framework import routers



urlpatterns = [
    url('admin/', admin.site.urls),
    url('tracking/', include('tracking.urls')),
    url(r'^api-auth/',include('rest_framework.urls')),
    url(r'^v1/', include('login.urls')),
]
