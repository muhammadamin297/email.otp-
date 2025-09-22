
from rest_framework import serializers
from configapp.models import *
from django.core.cache import cache
from django.contrib.auth.hashers import make_password
import random

class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'email','is_active','password', 'is_student', 'is_teacher','is_admin']
        read_only_fields = ['password']

    def create(self, validated_data):
        email = validated_data.get("email")
        cached_password = cache.get(f"{email}_password")
        if validated_data.get("password"):
            validated_data["password"] = make_password(validated_data["password"])
        elif cached_password:
            validated_data["password"] = make_password(cached_password)
            cache.delete(f"{email}_password")
        else:
            default_pass = str(random.randint(1000, 9999))
            validated_data["password"] = make_password(default_pass)
        return super().create(validated_data)

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
        read_only_fields = ['user']
class TeacherAndUserSerializer(serializers.Serializer):
    user = UserSerializer()
    teacher = TeacherSerializer()
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ['user']
class StudentAndUserSerializer(serializers.Serializer):
    user = UserSerializer()
    student = StudentSerializer()

class SendEmail(serializers.Serializer):
    email = serializers.EmailField()
class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    verify_kod =serializers.CharField()

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"



