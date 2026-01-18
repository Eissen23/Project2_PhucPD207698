from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import traceback
from teach_subject.serializers import TeacherSubjectSerializer
from teach_subject.models import Teachers, TeacherSubjects


# Create your views here.
class TeacherSubjectsView(APIView):
    serializer_class = TeacherSubjectSerializer

    def get(self, request, format=None):
        try:
            user = request.user
            if not user.is_teacher:
                return Response({'error': 'User does not have necessary permission'}, status=status.HTTP_403_FORBIDDEN)

            teacher = Teachers.objects.get(user_id=user.id)
            teacher_id = teacher.id

            subject_teacher = TeacherSubjects.objects.filter(magv=teacher_id)
            subject = self.serializer_class(data=subject_teacher, many=True)
            subject.is_valid()

            return Response({'classes': subject.data}, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )