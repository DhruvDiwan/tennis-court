from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from attendance.models import AttendancePerson, Batch
from django.core.exceptions import PermissionDenied
from attendance.forms import AttendancePersonForm

class AttendancePersonCreateView(CreateView):
    form_class = AttendancePersonForm
    success_url = reverse_lazy('attendance_person_new')
    template_name = 'person/attendance_person_new.html'

class AttendancePersonListView(LoginRequiredMixin , ListView):
    model = AttendancePerson
    template_name = 'person/attendance_person_list.html'
    login_url = 'login'

class AttendancePersonDetailView(LoginRequiredMixin , DetailView):
    model = AttendancePerson
    template_name = 'person/attendance_person_detail.html'
    login_url = 'login'

class AttendancePersonDeleteView(LoginRequiredMixin , DeleteView):
    model = AttendancePerson
    template_name = 'person/attendance_person_delete.html'
    success_url = reverse_lazy('attendance_person_list')
    login_url = 'login'

    def dispatch(self , request , *args , **kwargs):
        batches = Batch.objects.all()
        coaches = []
        for batch in batches:
            coaches += batch.coaches.all()
        if self.request.user not in coaches:
            raise PermissionDenied
        return super().dispatch(request , *args , **kwargs)

class AttendancePersonUpdateView(LoginRequiredMixin , UpdateView):
    model = AttendancePerson
    fields = '__all__'
    template_name = 'person/attendance_person_edit.html'
    login_url = 'login'

    def dispatch(self , request , *args , **kwargs):
        batches = Batch.objects.all()
        coaches = []
        for batch in batches:
            coaches += batch.coaches.all()
        if self.request.user not in coaches:
            raise PermissionDenied
        return super().dispatch(request , *args , **kwargs)
