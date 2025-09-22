from configapp.Permission import IsEmailVerified,IsAdmin
from configapp.models import *
from configapp.serializers import StudentSerializer,UserSerializer,StudentAndUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
class StudentDetailApi(ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [IsEmailVerified,IsAdmin]
    def get_serializer_class(self):
        if self.action in ["list", "retrieve","update","destroy"]:
            return StudentSerializer
        return StudentAndUserSerializer

    def create(self,request,*args,**kwargs):
        user_data = request.data.get('user',None)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save(is_student = True)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        student = request.data.get('student',None)
        student_serializer = StudentSerializer(data=student)
        if student_serializer.is_valid(raise_exception=True):
            student_serializer.save(user = user)
        else:
            user.delete()
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "user": user_serializer.data,
            "student": student_serializer.data
        }, status=status.HTTP_201_CREATED)

