import traceback
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from authentication.models import Students, Teachers, UserAccount
from authentication.serializers import SignupSerializer, UserSerializer, TeacherSerializer, StudentSerializer
from django.contrib.auth import get_user_model

from common.responses import ApiResponse

User = get_user_model()
# Create your views here.

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        serialized = self.serializer_class(data=request.data)

        if not serialized.is_valid():
            return ApiResponse.error(
                serialized.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        try:
            validated_data = serialized.validated_data
            email = validated_data['email'].lower()
            full_name = validated_data['full_name']
            password = validated_data['password']
            is_teacher = validated_data['is_teacher']

            if User.objects.filter(email=email).exists():
                return Response(
                    {'error': 'Email already exists'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user = UserAccount(fullName=full_name, email=email, password=password, is_teacher=is_teacher)
            self.insert_user_data(validated_data, user, is_teacher)

            user_type = "Teacher" if is_teacher else "User"
            return ApiResponse.success(
                message="{user_type} successfully created",
                status_code=status.HTTP_201_CREATED
            )

        except ValidationError as e:
            return ApiResponse.error(
                {'error': str(e)},
                status_code=status.HTTP_400_BAD_REQUEST
            )
        except RuntimeError as e:
            return ApiResponse.error(
                'Something went wrong',
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
     
class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            user_id = user.data['id']
            
            if not user.data['is_teacher']:
                user_detail = Students.objects.get(user_id = user_id)
                detail = StudentSerializer(user_detail)
                
            else:
                user_detail = Teachers.objects.get(user_id = user_id)
                detail = TeacherSerializer(user_detail)
            
            return Response(
                {
                    'user': user.data,
                    'detail': detail.data
                },
                status=status.HTTP_200_OK
            )
            
        except Exception:
            traceback.print_exc()
            return Response(
                {'error': 'Something went wrong'},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )