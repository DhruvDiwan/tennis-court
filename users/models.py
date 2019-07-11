from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=False, unique=True)
    FirstName = models.CharField(null=False, verbose_name="First Name" , max_length=300)
    Surname = models.CharField(null=False, max_length=300)
    
