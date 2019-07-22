from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from attendance.models import Batch
from django.core.exceptions import PermissionDenied

class BatchListView(LoginRequiredMixin , ListView):
    model = Batch
    template_name = 'batch/batch_list.html'
    login_url = 'login'

class BatchDetailView(LoginRequiredMixin , DetailView):
    model = Batch
    template_name = 'batch/batch_detail.html'
    login_url = 'login'

class BatchDeleteView(LoginRequiredMixin , DeleteView):
    model = Batch
    template_name = 'batch/batch_delete.html'
    success_url = reverse_lazy('batch_list')
    login_url = 'login'

    def dispatch(self , request , *args , **kwargs):
        batch = self.get_object()
        if self.request.user not in batch.coaches.all():
            raise PermissionDenied
        return super().dispatch(request , *args , **kwargs)

class BatchCreateView(LoginRequiredMixin , CreateView):
    model = Batch
    template_name = 'batch/batch_new.html'
    fields = '__all__'
    login_url = 'login'

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BatchUpdateView(LoginRequiredMixin , UpdateView):
    model = Batch
    fields = '__all__'
    template_name = 'batch/batch_edit.html'
    login_url = 'login'

    def dispatch(self , request , *args , **kwargs):
        batch = self.get_object()
        if self.request.user not in batch.coaches.all():
            raise PermissionDenied
        return super().dispatch(request , *args , **kwargs)
