from rest_framework import serializers
from group.models import StudentGroups, GroupMembers

class StudentGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroups
        fields = ('term', 'project_title', 'teacher_subject')


class GroupMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembers
        fields = ('id', 'group_id', 'student')


