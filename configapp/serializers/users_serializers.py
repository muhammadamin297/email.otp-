from rest_framework import serializers
from configapp.models import *
class UserSerializer(serializers.ModelSerializer):
    # is_active = serializers.BooleanField(read_only=True)
    # is_teacher = serializers.BooleanField(read_only=True)
    # is_admin = serializers.BooleanField(read_only=True)
    # is_student = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ['phone_number', 'email','is_active','password', 'is_student', 'is_teacher',]
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



