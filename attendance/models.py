from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import CustomUser

class AttendancePerson(models.Model):
    first_name = models.CharField(null = True, max_length=300)
    last_name = models.CharField(null = True, blank = True, max_length=300)
    middle_name = models.CharField(null = True, blank = True, max_length=300)
    date_of_birth = models.DateField(null = True, blank = True)
    mobile = PhoneNumberField(null = True, blank = True)
    telephone = PhoneNumberField(null = True, blank = True)
    intercom = models.CharField(null = True, blank = True, max_length=300)
    user = models.ForeignKey(CustomUser, blank = True, null = True, on_delete = models.CASCADE,)
    # relations = models.ForeignKey(CustomUser, on_delete = models.CASCADE,)

    def name(self):
        n = self.first_name
        if self.middle_name:
            n += " " + self.middle_name
        if self.last_name:
            n += " " + self.last_name
        return n

    def __str__(self):
        return self.name()

class Batch(models.Model):
    students = models.ManyToManyField(AttendancePerson)
    batch_name = models.CharField(null = True, max_length=300)

    def __str__(self):
        return self.batch_name

class ClassItem(models.Model):
    name = models.CharField(null = True, max_length=300)
    students = models.ManyToManyField(AttendancePerson)

class AttendanceList(models.Model):
    student = models.ForeignKey(AttendancePerson, on_delete = models.CASCADE,)
    class_item = models.ForeignKey(ClassItem, on_delete = models.CASCADE,)
