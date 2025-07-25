from django.urls import path
from .views import  CreateMeeting, ManageReport

urlpatterns = [

    path('createmeeting', CreateMeeting.as_view()),
    path('managereport', ManageReport.as_view()),
]