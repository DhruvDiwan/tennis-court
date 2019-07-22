from django.urls import path

from .views import (
    AttendancePersonCreateView,
    AttendancePersonListView,
    AttendancePersonDetailView,
    AttendancePersonUpdateView,
    AttendancePersonDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/',AttendancePersonUpdateView.as_view(), name='attendance_person_edit'),
    path('<int:pk>/',AttendancePersonDetailView.as_view(), name='attendance_person_detail'),
    path('<int:pk>/delete/', AttendancePersonDeleteView.as_view(), name='attendance_person_delete'),
    path('new/', AttendancePersonCreateView.as_view(), name='attendance_person_new'),
    path('', AttendancePersonListView.as_view(), name='attendance_person_list'),
]
