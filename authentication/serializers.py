from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from authentication.models import Students, UserAccount
from teach_subject.models import Teachers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id','fullName', 'email', 'is_teacher', )


class SignupSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    re_password = serializers.CharField(write_only=True, required=True)
    is_teacher = serializers.BooleanField(default=False, required=False)

    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError({'re_password': 'Passwords do not match'})
        return data

class AuthenticateSerializer(LoginSerializer):
    username = None

    def authenticate(self, **options):
        return authenticate(self.context["request"], **options)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                if  User.objects.filter(email=email).exists():
                    user = authenticate(email=email, password=password)
                else:
                    raise serializers.ValidationError({'email': 'Email address is not valid'}, code='authorization')
                if not user:
                    msg = "Invalid credentials."
                    raise serializers.ValidationError(msg, code="authorization")

            except ObjectDoesNotExist:
                    raise serializers.ValidationError('Invalid credential', code='authorization')
        else:
            msg = "No email provided."
            raise serializers.ValidationError(msg)
        attrs["user"] = user

        return attrs

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'phone', 'user_account' )

class TeacherSerializer (serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('id', 'institute', 'joined_since', 'status', 'user_account')

