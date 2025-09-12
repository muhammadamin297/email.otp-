from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from configapp.models import Teacher
from configapp.serializers import TeacherSerializer


class TeacherDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherListApi(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

