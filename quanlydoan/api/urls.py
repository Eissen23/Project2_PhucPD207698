from django.urls import path
from .views import SignupView, RetrieveUserView, CreateProjectGroup, AddStudentGroup, CreateMeeting

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('me', RetrieveUserView.as_view()),
    path('creategroup', CreateProjectGroup.as_view()),
    path('addstudent', AddStudentGroup.as_view()),
    path('createmeeting', CreateMeeting.as_view()),
]