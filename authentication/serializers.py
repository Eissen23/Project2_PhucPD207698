
from rest_framework import serializers
from django.contrib.auth import get_user_model

from authentication.models import Students, UserAccount
from teach_subject.models import Teachers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id','fullName', 'email', 'is_teacher', )


class SignupSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    re_password = serializers.CharField(write_only=True, required=True)
    is_teacher = serializers.BooleanField(default=False)

    def validate(self, data):
        if data['password'] != data['re_password']:
            raise serializers.ValidationError({'re_password': 'Passwords do not match'})
        return data

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id', 'phone', 'user_id' )
        
class TeacherSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Teachers
        fields = ('id', 'institute', 'joined_since', 'status', 'user_id')