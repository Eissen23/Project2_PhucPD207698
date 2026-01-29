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
            email = validated_data['email']
            full_name = validated_data['full_name']
            password = validated_data['password']
            is_teacher = validated_data['is_teacher']

            if User.objects.filter(email=email).exists():
                return ApiResponse.error(
                    'Email already exists',
                    status_code=status.HTTP_400_BAD_REQUEST
                )

            user = User(fullName=full_name, email=email, is_teacher=is_teacher)
            user.set_password(password)
            user.save()

            return ApiResponse.success(
                message="User successfully created",
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
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer



    def get(self, request, format=None):
        try:
            user = request.user
            user_data = self.serializer_class(user).data

            mapping = {
                True: (Teachers, TeacherSerializer),
                False: (Students, StudentSerializer)  # Fixed the serializer mismatch here
            }
            model_class, serializer_class = mapping.get(user.is_teacher)
            user_detail = model_class.objects.filter(user_account=user).first()
            detail_data = serializer_class(user_detail).data if user_detail else {}

            return Response(
                {
                    'user': user_data,
                    'detail': detail_data
                },
                status=status.HTTP_200_OK
            )

        except (Students.DoesNotExist, Teachers.DoesNotExist):
            return Response(
                {'error': 'User profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        except RuntimeError as e:
            # Log the error in production
            return Response(
                {'error': 'Something went wrong'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )