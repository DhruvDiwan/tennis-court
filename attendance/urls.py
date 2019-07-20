from django.urls import path
from django.views.generic import TemplateView

from .views import (
    AttendancePersonCreateView,
)

from .views import (
    BatchListView,
    BatchUpdateView,
    BatchDetailView,
    BatchDeleteView,
    BatchCreateView
)
urlpatterns = [
    path('', TemplateView.as_view(template_name="app_base.html"), name='attendance_home'),
]

urlpatterns += [
    path('batch/<int:pk>/edit/',BatchUpdateView.as_view(), name='batch_edit'),
    path('batch/<int:pk>/',BatchDetailView.as_view(), name='batch_detail'),
    path('batch/<int:pk>/delete/', BatchDeleteView.as_view(), name='batch_delete'),
    path('batch/new/', BatchCreateView.as_view(), name='batch_new'),
    path('batch/', BatchListView.as_view(), name='batch_list'),
]

urlpatterns += [
    # path('person/<int:pk>/edit/',AttendancePersonUpdateView.as_view(), name='attendance_person_edit'),
    # path('person/<int:pk>/',AttendancePersonDetailView.as_view(), name='attendance_person_detail'),
    # path('person/<int:pk>/delete/', AttendancePersonDeleteView.as_view(), name='attendance_person_delete'),
    path('person/new/', AttendancePersonCreateView.as_view(), name='attendance_person_new'),
    # path('person/', AttendancePersonListView.as_view(), name='attendance_person_list'),
]
