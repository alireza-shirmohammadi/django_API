from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

from .models import Login


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'
