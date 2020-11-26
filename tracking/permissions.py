from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission


class IsCourier(BasePermission):
    def has_permission(self, request, view=None):
        try:
            request.user.courier
        except (ObjectDoesNotExist, AttributeError):
            return False
        return True


class IsRestaurant(BasePermission):
    def has_permission(self, request, view=None):
        try:
            request.user.restaurant
        except (ObjectDoesNotExist, AttributeError):
            return False
        return True
