from django.contrib import admin
from .models import Person , MobNo , Username , Password

# Register your models here.
admin.site.register(Person)
admin.site.register(MobNo)
admin.site.register(Username)
admin.site.register(Password)
