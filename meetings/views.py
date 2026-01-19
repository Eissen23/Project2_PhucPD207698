import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

from common.responses import ApiResponse
from group.models import StudentGroups
from meetings.models import Meetings, Reports
from meetings.serializers import ReportSerializer, MeetingSerializer


# Create your views here.
class MeetingsView(APIView):
    serializer_class = MeetingSerializer
    
    def post(self, request):
        try: 
            user= request.user
            if not user.is_teacher:
                return ApiResponse.error('Only student are allowed', status_code=status.HTTP_403_FORBIDDEN)

            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():

                group_id = serializer.data.get('group_id')
                group = StudentGroups.objects.get(id = group_id)

                if group is None:
                    raise serializers.ValidationError({'error': 'Group not found'})
                
                schedule_date = serializer.data.get('schedule_date')
                note = serializer.data.get('note_id')

                meeting = Meetings(id = id, group_id= group_id, schedule_date = schedule_date, note = note)
                meeting.save()

                return ApiResponse.success(self.serializer_class(meeting).data)
            
        except Exception:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'error': serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, format = None):
       try:
            
            data = request.data 

            group = StudentGroups.objects.get(id = data['group_id'])
            if group is None:
                raise serializers.ValidationError({'error': 'Group not found'})

            meetings = self.serializer_class(Meetings.objects.filter(group_id = group.id), many=True)
            meetings.is_valid()
            
            return ApiResponse.success(meetings.data)
       except Exception:
            traceback.print_exc()
            return Response({'error': "something wrong"}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReportsView(APIView):

    serializer_class = ReportSerializer

    def put(self, request):
        try:
            user = request.user
            if user.is_teacher: 
               return ApiResponse.error('Only student are allowed', status_code=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            
            meeting = Meetings.objects.get(id = data['meeting_id'])
            if meeting is None:
                raise serializers.ValidationError({'error': 'Meeting not found'})

            update_report = Reports.objects.get(id = data['id'])
            if update_report is None:
                raise serializers.ValidationError({'error': 'Report not found'})

            update_report.cloud_url = data['codeurl']
            update_report.report = data['report']
            update_report.meeting_id = data['meeting_id']

            update_report.save(update_fields=[
                "cloud_url",
                "report",
                "meeting_id",
            ])

            return ApiResponse.success(
                message='Listing updated successfully',
                status_code=status.HTTP_200_OK
            )
            
        except Exception: 
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    def get(self, request, format = None):
        try:
            user = request.user
            if not user.is_teacher:
                return Response({'error':'Only Teacher are allowed'}, status=status.HTTP_403_FORBIDDEN)
            
            data = request.data
            meeting_id = data['cuochop']
            meeting = Meetings.objects.get(id = meeting_id)
            
            
            report = Reports.objects.filter(cuochop = meeting)
            report = self.serializer_class(data = report)
            report.is_valid()
            
            return ApiResponse.success(report.data, "Listing report successfully")
            
        except Exception:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)