from rest_framework import serializers

from meetings.models import Cuochop, Report


class CuocHopSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Cuochop
        fields = ('idnhom', 'meettime', 'isreported','ghichu', )
        
        
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('codeurl','report', 'cuochop',)