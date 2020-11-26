from django.contrib import admin

from tracking.models import Courier, Restaurant


class CourierAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'user_id']


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'user_id']


admin.site.register(Courier, CourierAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
