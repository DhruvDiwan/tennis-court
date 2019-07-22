from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AttendancePersonForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
