from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AttendancePersonForm
class AttendancePersonCreateView(CreateView):
    form_class = AttendancePersonForm
    success_url = reverse_lazy('attendance person')
    template_name = 'attendancePerson.html'
