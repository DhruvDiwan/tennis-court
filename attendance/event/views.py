from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from attendance.models import AttendanceEvent, Batch
from django.core.exceptions import PermissionDenied

class AttendanceEventListView(LoginRequiredMixin , ListView):
    model = AttendanceEvent
    template_name = 'event/attendance_event_list.html'
    login_url = 'login'

class AttendanceEventDetailView(LoginRequiredMixin , DetailView):
    model = AttendanceEvent
    template_name = 'event/attendance_event_detail.html'
    login_url = 'login'

class AttendanceEventDeleteView(LoginRequiredMixin , DeleteView):
    model = AttendanceEvent
    template_name = 'event/attendance_event_delete.html'
    success_url = reverse_lazy('attendance_event_list')
    login_url = 'login'

    def dispatch(self , request , *args , **kwargs):
        batches = Batch.objects.all()
        coaches = []
        for batch in batches:
            coaches += batch.coaches.all()
        if self.request.user not in coaches:
            raise PermissionDenied
        return super().dispatch(request , *args , **kwargs)

class AttendanceEventCreateView(LoginRequiredMixin , CreateView):
    model = AttendanceEvent
    template_name = 'event/attendance_event_new.html'
    fields = '__all__'
    login_url = 'login'

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AttendanceEventUpdateView(LoginRequiredMixin , UpdateView):
    model = AttendanceEvent
    fields = '__all__'
    template_name = 'event/attendance_event_edit.html'
    login_url = 'login'

    def dispatch(self , request , *args , **kwargs):
        batches = Batch.objects.all()
        coaches = []
        for batch in batches:
            coaches += batch.coaches.all()
        if self.request.user not in coaches:
            raise PermissionDenied
        return super().dispatch(request , *args , **kwargs)
