from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from tracking.permissions import IsCourier, IsRestaurant
from tracking.serializers import CourierSerializer, RestaurantSerializer


class CourierInfo(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsCourier]
    serializer_class = CourierSerializer

    def get_object(self):
        return self.request.user.courier


class RestaurantInfo(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsRestaurant]
    serializer_class = RestaurantSerializer

    def get_object(self):
        return self.request.user.restaurant
