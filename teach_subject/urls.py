from django.urls import path
from teach_subject.views import TeacherSubjectsView

urlpatterns = [
    path('',TeacherSubjectsView.as_view(), name='teach_subject'),
]