from django.urls import path

from .views import (
    AttendanceEventCreateView,
    AttendanceEventListView,
    AttendanceEventDetailView,
    AttendanceEventUpdateView,
    AttendanceEventDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/',AttendanceEventUpdateView.as_view(), name='attendance_event_edit'),
    path('<int:pk>/',AttendanceEventDetailView.as_view(), name='attendance_event_detail'),
    path('<int:pk>/delete/', AttendanceEventDeleteView.as_view(), name='attendance_event_delete'),
    path('new/', AttendanceEventCreateView.as_view(), name='attendance_event_new'),
    path('', AttendanceEventListView.as_view(), name='attendance_event_list'),
]
