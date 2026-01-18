from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.models import Students, UserAccount
from common.responses import ApiResponse
from group.models import  StudentGroups, GroupMembers
from django.contrib.auth import get_user_model
import traceback
from api.utilities.id_generator import id_generator
from group.serializers import GroupMembersSerializer
from teach_subject.models import TeacherSubjects

User = get_user_model()

class ManageStudentGroup(APIView):

    serializer_class = GroupMembersSerializer
    def post(self, request):
        try:
            
            user = request.user
            
            if not user.is_teacher:
                return Response({'error': 'User does not have necessary permission' }, status=status.HTTP_403_FORBIDDEN)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():

                student_id = serializer.data.get('student_id')
                student = Students.objects.get(id = student_id)

                if student is None:
                    raise serializers.ValidationError({'error': 'Student not found'})
                
                student_group_id = serializer.data.get('group_id')
                group = StudentGroups.objects.get(id = student_group_id)

                if group is None:
                    raise serializers.ValidationError({'error': 'Student group not found'})

                group_member = GroupMembers( student_id = student_id, group_id= student_group_id)
                group_member.save()

                return ApiResponse.success(GroupMembersSerializer(group_member).data)
            
            return Response({'error': 'Something went wrong'}, status= status.HTTP_400_BAD_REQUEST)
            
        except Exception:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
