from django.contrib.auth import authenticate
from rest_framework import serializers
from users.models import Authenticable, User, Profile
from notifications.tasks import send_welcome_email

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'

class AuthenticableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Authenticable
        fields = ['id', 'email']

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=30, write_only=True)
    description = serializers.CharField(max_length=500, write_only=True)
    country = serializers.CharField(max_length=2, write_only=True)
    phone = serializers.CharField(max_length=30, write_only=True)

    # Relations

    authenticable = AuthenticableSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'id', 'name', 'last_name', 'description', 'country', 'phone', 'authenticable', 'profile']

    def validate_email(self, value):
        if Authenticable.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exist")
        return value
    

    def create(self, validated_data):
        user = User.objects.create_complete_user(**validated_data)
        send_welcome_email.delay(
            user.authenticable.email,
            user.name,
            user.last_name
        )
        return user
