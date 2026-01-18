from django.urls import path

from group.views import ManageProjectGroup

urlpatterns = [
    path('', ManageProjectGroup.as_view()),
]