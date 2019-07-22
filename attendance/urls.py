from django.views.generic import TemplateView
from django.urls import path , include


urlpatterns = [
    path('', TemplateView.as_view(template_name="app_base.html"), name='attendance_home'),
    path('batch/' , include('attendance.batch.urls')),
    path('person/' , include('attendance.person.urls')),
    path('event/' , include('attendance.event.urls')),
    path('item/' , include('attendance.item.urls')),
]
