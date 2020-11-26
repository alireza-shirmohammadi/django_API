from django.core.validators import MinLengthValidator
from django.db import models


class Courier(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10,
                                     validators=[MinLengthValidator(10)],
                                     unique=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.user.get_full_name()


class Restaurant(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.title
