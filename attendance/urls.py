from django.urls import path
from .views import AttendancePersonCreateView
urlpatterns = [
    path('', AttendancePersonCreateView.as_view(), name='attendance person'),
]
