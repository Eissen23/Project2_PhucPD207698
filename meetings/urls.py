from django.urls import path
from .views import  CreateMeeting, ManageReport

urlpatterns = [

    path('meetings', CreateMeeting.as_view()),
    path('report', ManageReport.as_view()),
]