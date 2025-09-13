from rest_framework.viewsets import ModelViewSet
from configapp.models import Teacher
from configapp.serializers import TeacherSerializer,TeacherAndUserSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
class TeacherCreateApi(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherAndUserSerializer

    def create(self, request, *args, **kwargs):
        user_data = request.data.get('user', None)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save(is_teacher=True)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        teacher = request.data.get('teacher', None)
        teacher_serializer = TeacherSerializer(data=teacher)
        if teacher_serializer.is_valid():
            teacher_serializer.save(user=user)
        else:
            user.delete()
            return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "user": user_serializer.data,
            "teacher": teacher_serializer.data
        }, status=status.HTTP_201_CREATED)


