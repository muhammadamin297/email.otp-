from rest_framework import serializers
from configapp.models import *
class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ['phone_number', 'email','is_active','password', 'is_student', 'is_teacher',"is_admin",]
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['name','surname']
        read_only_fields = ['user']
class TeacherAndUserSerializer(serializers.Serializer):
    user = UserSerializer()
    teacher = TeacherSerializer()
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
