from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    middle_name = models.CharField(null = True, max_length=300)
    date_of_birth = models.DateField(null = True)
    mobile = PhoneNumberField(null = True)
    telephone = PhoneNumberField(null = True)
    intercom = models.CharField(null = True, max_length=300)
    # relations = models.ForeignKey(CustomUser, on_delete = models.CASCADE,)
