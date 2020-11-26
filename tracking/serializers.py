from rest_framework.serializers import ModelSerializer

from tracking.models import Courier, Restaurant


class CourierSerializer(ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
