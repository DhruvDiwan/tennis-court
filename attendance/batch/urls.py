from django.urls import path

from .views import (
    BatchListView,
    BatchUpdateView,
    BatchDetailView,
    BatchDeleteView,
    BatchCreateView
)

urlpatterns = [
    path('<int:pk>/edit/',BatchUpdateView.as_view(), name='batch_edit'),
    path('<int:pk>/',BatchDetailView.as_view(), name='batch_detail'),
    path('<int:pk>/delete/', BatchDeleteView.as_view(), name='batch_delete'),
    path('new/', BatchCreateView.as_view(), name='batch_new'),
    path('', BatchListView.as_view(), name='batch_list'),
]
