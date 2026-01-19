from django.urls import path

from group.views import GroupMembersView

urlpatterns = [
    path('', GroupMembersView.as_view()),
]