from django.urls import path

from .views import (
    AttendanceItemCreateView,
    AttendanceItemListView,
    AttendanceItemDetailView,
    AttendanceItemUpdateView,
    AttendanceItemDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/',AttendanceItemUpdateView.as_view(), name='attendance_item_edit'),
    path('<int:pk>/',AttendanceItemDetailView.as_view(), name='attendance_item_detail'),
    path('<int:pk>/delete/', AttendanceItemDeleteView.as_view(), name='attendance_item_delete'),
    path('new/', AttendanceItemCreateView.as_view(), name='attendance_item_new'),
    path('', AttendanceItemListView.as_view(), name='attendance_item_list'),
]
