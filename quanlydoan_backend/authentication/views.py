import traceback
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Giangvien, Sinhvien
from quanlydoan.authentication.serializers import SignupSerializer, UserSerializer, GiangvienSerializer, SinhvienSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            validated_data = serializer.validated_data
            email = validated_data['email'].lower()
            full_name = validated_data['full_name']
            password = validated_data['password']
            is_teacher = validated_data['is_teacher']

            if User.objects.filter(email=email).exists():
                return Response(
                    {'error': 'Email already exists'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user = self.create_user(full_name, email, password, is_teacher)
            self.insert_user_data(validated_data, user, is_teacher)

            user_type = "Teacher" if is_teacher else "User"
            return Response(
                {"success": f"{user_type} successfully created"},
                status=status.HTTP_201_CREATED
            )

        except ValidationError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            return Response(
                {'error': 'Something went wrong'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
     
class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            user_id = user.data['id']
            
            if not user.data['is_teacher']:
                user_detail = Sinhvien.objects.get(user_id = user_id) 
                detail = SinhvienSerializer(user_detail)
                
            else:
                user_detail = Giangvien.objects.get(user_id = user_id)
                detail = GiangvienSerializer(user_detail)
            
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