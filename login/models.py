from django.core.validators import MinLengthValidator
from django.db import models


class Login(models.Model):
    phone = models.CharField(max_length=10)
    token = models.CharField(max_length=4,blank=True)

    def __str__(self):
        return self.phone1
