from rest_framework import serializers
from configapp.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'email','is_active','password', 'is_student', 'is_teacher',"is_admin",]
        read_only_fields = ["sms_kod"]
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
