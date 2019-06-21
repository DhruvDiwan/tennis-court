from django.db import models

class Person(models.Model):
    fName = models.TextField()
    sName = models.TextField()
    # DOB = models.DateField()
    # grade = models.IntegerField(default = 0)
    # school = models.TextField(default = "")

    def __str__(self):
        return self.fName + " " + self.sName

class MobNo(models.Model):
    phone_number = models.CharField(max_length=10)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.phone_number

class Username(models.Model):
    username = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Password(models.Model):
    password = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.password
