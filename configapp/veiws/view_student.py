from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from configapp.models import Student
from configapp.serializers import StudentSerializer


class StudentDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

