from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import CustomUser
from django.urls import reverse

class AttendancePerson(models.Model):
    first_name = models.CharField(null = True, max_length=300)
    last_name = models.CharField(null = True, blank = True, max_length=300)
    middle_name = models.CharField(null = True, blank = True, max_length=300)
    date_of_birth = models.DateField(null = True, blank = True)
    mobile = PhoneNumberField(null = True, blank = True)
    telephone = PhoneNumberField(null = True, blank = True, max_length=300)
    user = models.ForeignKey(CustomUser, blank = True, null = True, on_delete = models.CASCADE,)
    # relations = models.ManyToManyField(CustomUser)
    title = models.CharField(null = True, max_length=300)
    subtitle = models.CharField(null = True, max_length=300)

    def name(self):
        n = self.first_name
        if self.middle_name:
            n += " " + self.middle_name
        if self.last_name:
            n += " " + self.last_name
        return n

    def __str__(self):
        return self.name()

    def get_absolute_url(self):
        return reverse('attendance_person_detail' , args = [str(self.id)])


class Batch(models.Model):
    '''
    A group of people for purpose of attendance
    '''
    students = models.ManyToManyField(AttendancePerson)
    batch_name = models.CharField(null = True, max_length=300)
    coaches = models.ManyToManyField(CustomUser)
    title = models.CharField(null = True, max_length=300)
    subtitle = models.CharField(null = True, max_length=300)

    def get_absolute_url(self):
        return reverse('batch_detail' , args = [str(self.id)])

    def __str__(self):
        return self.batch_name

class AttendanceEvent(models.Model):
    '''
    This is an Attendance Event
    '''
    name = models.CharField(null = True, max_length=300)
    students = models.ManyToManyField(AttendancePerson)
    batches = models.ManyToManyField(Batch)
    scheduled_date_time = models.DateTimeField(null = True, blank = True)
    execution_date_time = models.DateTimeField(null = True, blank = True)
    # event status options : scheduled , tentative , cancelled , on hold , on going , proposed
    event_status = models.CharField(null = True, max_length=300)

    def get_absolute_url(self):
        return reverse('attendance_event_detail' , args = [str(self.id)])

    def __str__(self):
        return self.name

class AttendanceItem(models.Model):
    '''
    This is an Attendance Item
    '''
    student = models.ForeignKey(AttendancePerson, on_delete = models.CASCADE,)
    attendance_event = models.ForeignKey(AttendanceEvent, on_delete = models.CASCADE,)
    # status options : present , absent , sick , leave , extend , guest , demo
    status = models.CharField(null = True, max_length=300)

    def get_absolute_url(self):
        return reverse('attendance_item_detail' , args = [str(self.id)])

    def __str__(self):
        return '\t'.join([self.student.name() , str(self.attendance_event) , self.status])


# class Telephone(models.Model):
#         telephone = PhoneNumberField(null = True, blank = True)
