from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstname','lastname','email','datetime', 'username', 'password')


class CustomRegisterSerializer(RegisterSerializer):
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('firstname','lastname','datetime','email', 'username', 'password', 'is_staff', 'is_superuser')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'is_staff': self.validated_data.get('is_staff', ''),
            'is_superuser': self.validated_data.get('is_superuser', ''),
            'firstname': self.validated_data.get('firstname', ''),
            'lastname': self.validated_data.get('lastname', ''),
            'datetime': self.validated_data.get('datetime', ''),
            
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_staff = self.cleaned_data.get('is_staff')
        user.is_superuser = self.cleaned_data.get('is_superuser')
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()
    
    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_superuser = serializer_data.get('is_superuser')
        is_staff = serializer_data.get('is_staff')
        return {
            'is_superuser': is_superuser,
            'is_staff' : is_staff
        }
 