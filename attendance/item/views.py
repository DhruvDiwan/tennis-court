from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from attendance.models import AttendanceItem, Batch
from django.core.exceptions import PermissionDenied

class AttendanceItemListView(LoginRequiredMixin , ListView):
    model = AttendanceItem
    template_name = 'item/attendance_item_list.html'
    login_url = 'login'

class AttendanceItemDetailView(LoginRequiredMixin , DetailView):
    model = AttendanceItem
    template_name = 'item/attendance_item_detail.html'
    login_url = 'login'

class AttendanceItemDeleteView(LoginRequiredMixin , DeleteView):
    model = AttendanceItem
    template_name = 'item/attendance_item_delete.html'
    success_url = reverse_lazy('attendance_item_list')
    login_url = 'login'

    def dispatch(self , request , *args , **kwargs):
        batches = Batch.objects.all()
        coaches = []
        for batch in batches:
            coaches += batch.coaches.all()
        if self.request.user not in coaches:
            raise PermissionDenied
        return super().dispatch(request , *args , **kwargs)

class AttendanceItemCreateView(LoginRequiredMixin , CreateView):
    model = AttendanceItem
    template_name = 'item/attendance_item_new.html'
    fields = '__all__'
    login_url = 'login'

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AttendanceItemUpdateView(LoginRequiredMixin , UpdateView):
    model = AttendanceItem
    fields = '__all__'
    template_name = 'item/attendance_item_edit.html'
    login_url = 'login'

    def dispatch(self , request , *args , **kwargs):
        batches = Batch.objects.all()
        coaches = []
        for batch in batches:
            coaches += batch.coaches.all()
        if self.request.user not in coaches:
            raise PermissionDenied
        return super().dispatch(request , *args , **kwargs)
