from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import url

urlpatterns = [
    path('login/', views.login_API),
    path('login/confirm/', views.login_confirm),
]
