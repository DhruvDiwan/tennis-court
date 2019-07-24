from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from attendance.models import AttendanceEvent, Batch, AttendanceItem
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class AttendanceEventListView(LoginRequiredMixin , ListView):
    model = AttendanceEvent
    template_name = 'event/attendance_event_list.html'
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

@login_required
def AttendanceEventDetailView(request, event_id):
    event = AttendanceEvent.objects.get(id = event_id)
    students = event.students.all()
    if request.method == 'POST':
        for student in students:
            if not f'{student.id}_ai' in request.POST.keys():
                continue
            attendance_mark = request.POST[f'{student.id}_ai']
            match = AttendanceItem.objects.filter(student = student, attendance_event = event)
            if(match):
                ai = match[0]
                ai.status = attendance_mark
                ai.save()
            else:
                ai = AttendanceItem.objects.create(student = student, attendance_event = event, status = attendance_mark)
                ai.save()
        return HttpResponseRedirect('/attendance/event/')
    # if a GET (or any other method) we'll create a blank form
    else:
        students_status = {}
        for student in students:
            match = AttendanceItem.objects.filter(student = student, attendance_event = event)            
            if match:
                students_status[student.id] = match[0].status
        return render(request, 'event/attendance_event_detail.html', 
                      {
                          'students': students, 
                          'event' : event,
                          'students_status' : students_status,
                      }
                     )
