from cProfile import label
from tkinter import Widget
from django.forms import PasswordInput, ValidationError
from rest_framework import serializers
from users.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    
class GetUsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email']