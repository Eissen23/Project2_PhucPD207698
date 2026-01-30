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
        fields = ('id','full_name', 'email', 'is_teacher', )

class CurrentUserSerializer(serializers.Serializer):
    detail = serializers.SerializerMethodField()
    def to_representation(self, user):
        return {
            "user": UserSerializer(user).data,
            "detail": self.get_detail(user),
        }

    def get_detail(self, obj):
        if obj.is_teacher:
            instance = Teachers.objects.filter(user_account=obj).first()
            return TeacherSerializer(instance).data if instance else {}
        instance = Students.objects.filter(user_account=obj).first()
        return StudentSerializer(instance).data if instance else {}


class SignupSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    re_password = serializers.CharField(write_only=True, required=True)
    is_teacher = serializers.BooleanField(default=False, required=False)

    # Validate
    def validate(self, data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists")
        if data['password'] != data['re_password']:
            raise serializers.ValidationError({'re_password': 'Passwords do not match'})
        return data

    # Create data
    def create(self, data):
        user = UserAccount(
            full_name=data['full_name'],
            email=data['email'],
            is_teacher=data['is_teacher'],
        )
        user.set_password(data['password'])
        user.save()

        return user


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
        fields = ('id', 'phone')
        read_only_fields = ('id',)

class TeacherSerializer (serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('id', 'institute', 'joined_since', 'status')
        read_only_fields = ('id',)


# info
class ProfileCreateSerializer(serializers.Serializer):
    # union of all possible fields
    phone = serializers.CharField(required=False)
    institute = serializers.CharField(required=False)
    joined_since = serializers.DateField(required=False)
    status = serializers.CharField(required=False)

    def validate(self, attrs):
        user = self.context['request'].user

        if user.is_teacher:
            required = {'institute', 'joined_since', 'status'}
        else:
            required = {'phone'}

        missing = required - attrs.keys()
        if missing:
            raise serializers.ValidationError(
                {field: 'This field is required.' for field in missing}
            )

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user

        if user.is_teacher:
            if Teachers.objects.filter(user_account=user).exists():
                raise serializers.ValidationError('Teacher profile already exists')

            return Teachers.objects.create(
                user_account=user,
                **validated_data
            )

        else:
            if Students.objects.filter(user_account=user).exists():
                raise serializers.ValidationError('Student profile already exists')

            return Students.objects.create(
                user_account=user,
                **validated_data
            )