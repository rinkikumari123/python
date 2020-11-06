from rest_framework import serializers
from django.db import models
from testapp.models import Student, AdminRegistraion
from rest_framework import serializers
from django.contrib.auth.models import User

'''
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminRegistraion
        extra_kwargs = {'password': {'write_only': True}}
        fields = ["id","name","phone_no","email_id","city","gender","password",]


        def create(self, validated_data):
            user = models.AdminRegistraion(
                name = validated_data['name'],
                phone_no = validated_data['phone_no'],
                email_id = validated_data['email_id'],
                city = validated_data['city'],
                gender = validated_data['gender'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminRegistraion
        fields =["email_id", "password"]
'''


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields = ["id","name","marks","roll_num","created_date","city","updated_By","updated_date"]

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
