from django.forms import ModelForm
from .models import AttendancePerson

class AttendancePersonForm(ModelForm):
    class Meta:
        model = AttendancePerson
        # fields = ('first_name', 'middle_name', 'last_name')
        fields = '__all__'
