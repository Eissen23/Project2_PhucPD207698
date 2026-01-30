from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, serializers
import traceback

from authentication.models import Students
from common.responses import ApiResponse
from group.models import StudentGroups, GroupMembers
from group.serializers import GroupMembersSerializer, StudentGroupsSerializer
from teach_subject.models import Teachers, TeacherSubjects
from teach_subject.serializers import TeacherSubjectSerializer


# Create your views here.
class GroupMembersView(APIView):
    serializer_class = GroupMembersSerializer

    def post(self, request):
        try:

            user = request.user

            if not user.is_teacher:
                return Response({'error': 'User does not have necessary permission'}, status=status.HTTP_403_FORBIDDEN)

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():

                student_id = serializer.data.get('student_id')
                student = Students.objects.get(id=student_id)

                if student is None:
                    raise serializers.ValidationError({'error': 'Student not found'})

                student_group_id = serializer.data.get('group_id')
                group = StudentGroups.objects.get(id=student_group_id)

                if group is None:
                    raise serializers.ValidationError({'error': 'Student group not found'})

                group_member = GroupMembers(student_id=student_id, group_id=student_group_id)
                group_member.save()

                return ApiResponse.success(GroupMembersSerializer(group_member).data)

            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

        except RuntimeError:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class StudentGroupsView(APIView):
    serializer_class = StudentGroupsSerializer

    def post(self, request):
        try:
            user = request.user

            if not user.is_teacher:
                return Response({'error': 'User does not have necessary permission'}, status=status.HTTP_403_FORBIDDEN)

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                term = serializer.data.get('term')
                group_name = serializer.data.get('group_name')
                teacher_id = serializer.data.get('teacher_id')

                student_group = StudentGroups(term=term, group_name=group_name, lead_teacher=teacher_id)
                student_group.save()

                return ApiResponse.success(data=self.serializer_class(student_group).data,
                                           message="Successfully added student group")

            return Response({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

        except RuntimeError:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # get the list of project group for each the student and teacher
    def get(self,
            request,
            format=None):
        try:
            user = request.user

            group_id = request.query_params.get('group_id')
            project_group = []

            # for the teacher side
            if user.is_teacher:
                teacher_id = Teachers.objects.get(user_id=user.id).id

                if group_id is None:

                    teacher_subject = TeacherSubjectSerializer(
                        data=TeacherSubjects.objects.order_by('subject_id').filter(teacher_id=teacher_id),
                        many=True
                    )

                    teacher_subject.is_valid()
                    for subject in teacher_subject.data:
                        student_group = StudentGroups.objects.get(lead_teacher=subject.get('lead_teacher'))
                        project_group.append(self.serializer_class(student_group).data)

                    return Response({'student_groups': project_group}, status=status.HTTP_200_OK)

            else:
                student_id = Students.objects.get(user_id=user.id).id

                if not group_id:
                    group_member = GroupMembers.objects.filter(student_id=student_id)
                    group_member = GroupMembersSerializer(data=group_member, many=True)

                    group_member.is_valid()
                    for group in group_member.data:
                        project_group.append(self.serializer_class(
                            StudentGroups.objects.get(
                                id=group.get('group_id'))
                        ).data)

                    return ApiResponse.success( project_group, status_code=status.HTTP_200_OK)

        except RuntimeError:
            traceback.print_exc()
            return ApiResponse.error('Some exeption happened', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)