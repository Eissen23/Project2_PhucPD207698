from django.urls import path
from .views import SignupView, RetrieveUserView, ManageProjectGroup, ManageStudentGroup, ManageClass, CreateMeeting

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('me', RetrieveUserView.as_view()),
    path('managegroup', ManageProjectGroup.as_view()),
    path('managestudent', ManageStudentGroup.as_view()),
    path("manageclass", ManageClass.as_view()),
    path('createmeeting', CreateMeeting.as_view()),
]