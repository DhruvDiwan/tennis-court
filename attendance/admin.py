from django.contrib import admin
from .models import AttendancePerson, Batch, ClassItem, AttendanceList

admin.site.register(AttendancePerson)
admin.site.register(Batch)
admin.site.register(ClassItem)
admin.site.register(AttendanceList)
