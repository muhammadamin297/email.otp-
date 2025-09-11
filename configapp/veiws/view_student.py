from configapp.models import Student
from configapp.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet

class StudentApi(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
