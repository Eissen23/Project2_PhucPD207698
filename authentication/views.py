import traceback

from dj_rest_auth.views import LoginView, LogoutView
from django.forms import ValidationError
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import permissions, status
from authentication.serializers import SignupSerializer, CurrentUserSerializer, ProfileCreateSerializer
from django.contrib.auth import get_user_model

from common.responses import ApiResponse

User = get_user_model()
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return ApiResponse.error(
                serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()

        return ApiResponse.success(
            message="Signup successful",
            data=serializer.data,
            status_code=status.HTTP_201_CREATED
        )


# The login view inherited from dj_rest_auth.LoginView
class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        response_data = {
            "access_token": response.data["access"],
            "access_expires": response.data["access_expiration"],
            "refresh_token": response.data["refresh"],
            "refresh_expires": response.data["refresh_expiration"],
            "user": response.data["user"]
        }

        return ApiResponse.success(message="Login successful", data=response_data)

class RetrieveUserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrentUserSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return ApiResponse.success(serializer.data)


class ProfileCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileCreateSerializer