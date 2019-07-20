from django.contrib import admin
from .models import AttendancePerson, Batch, AttendanceEvent, AttendanceItem

admin.site.register(AttendancePerson)
admin.site.register(Batch)
admin.site.register(AttendanceEvent)
admin.site.register(AttendanceItem)
