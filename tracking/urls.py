from django.urls import path
from . import views

urlpatterns = [
    path('couriers/me/', views.CourierInfo.as_view()),
    path('restaurants/me/', views.RestaurantInfo.as_view()),
]
