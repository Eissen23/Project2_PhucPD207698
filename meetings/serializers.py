from rest_framework import serializers

from meetings.models import Meetings, Reports


class MeetingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Meetings
        fields = ('id', 'schedule_date', 'student_group','note', )
        
        
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ('id', 'cloud_url', 'report', 'meeting',)