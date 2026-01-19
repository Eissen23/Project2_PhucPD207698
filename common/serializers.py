from rest_framework import serializers


# FOR Dj_auth
# More at: https://dj-rest-auth.readthedocs.io/en/latest/configuration.html
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)