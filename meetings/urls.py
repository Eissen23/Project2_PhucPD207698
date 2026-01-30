from django.urls import path
from .views import  MeetingsView, ReportsView

urlpatterns = [
    path('', MeetingsView.as_view()),
    path('reports', ReportsView.as_view()),
]