from django.urls import path
from .views import  ManageStudentGroup

urlpatterns = [
    path('managestudent', ManageStudentGroup.as_view()),
    path("manageclass", ManageClass.as_view()),
]