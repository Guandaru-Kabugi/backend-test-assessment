from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 'confirm_password']
        read_only_fields = ['id']
    def validate(self, attrs):

        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({"password": "Password fields didn't match."}) #a way to check if the password and confirm password are the same
        try:
            validate_password(attrs.get('password')) #exception handling for password validation
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)}) #checking errors by using validationerror, which is part of django.core.exceptions
        attrs
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm_password', None) #removing the confirm password field from the validated data
        password = validated_data.pop('password', None) #removing the password field from the validated data
        user = User(**validated_data) #creating a new user instance with the validated data
        user.set_password(password) #setting the password for the user instance by hashing it
        user.save()
        return user