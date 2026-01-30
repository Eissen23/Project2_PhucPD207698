from django.urls import path

from group.views import GroupMembersView, StudentGroupsView

urlpatterns = [
    path('member', GroupMembersView.as_view()),
    path('', StudentGroupsView.as_view()),
]