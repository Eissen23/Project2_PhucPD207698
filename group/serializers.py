from rest_framework import serializers
from group.models import StudentGroups, GroupMembers

class StudentGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroups
        fields = ('term', 'group_name', 'lead_teacher')


class GroupMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembers
        fields = ('id', 'group_id', 'student_id')


