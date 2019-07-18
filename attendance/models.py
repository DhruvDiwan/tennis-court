from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField

class AttendancePerson(models.Model):
    first_name = models.CharField(null = True, max_length=300)
    last_name = models.CharField(null = True, max_length=300)
    middle_name = models.CharField(null = True, max_length=300)
    date_of_birth = models.DateField(null = True)
    address = AddressField(null = True, on_delete = models.CASCADE)
    mobile = PhoneNumberField(null = True)
    telephone = PhoneNumberField(null = True)
    intercom = models.CharField(null = True, max_length=300)
    # relations = models.ForeignKey(CustomUser, on_delete = models.CASCADE,)

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name

class Batch(models.Model):
    students = models.ManyToManyField(AttendancePerson)
    batch_name = models.CharField(null = True, max_length=300)

    def __str__(self):
        return self.batch_name
