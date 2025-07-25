from django.urls import path
from .views import ManageProjectGroup, ManageStudentGroup, ManageClass

urlpatterns = [
    path('managegroup', ManageProjectGroup.as_view()),
    path('managestudent', ManageStudentGroup.as_view()),
    path("manageclass", ManageClass.as_view()),
]