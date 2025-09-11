from rest_framework import status

from configapp.models import User,Student,Teacher
from configapp.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
class UserApi(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop("password")
        user = User(**serializer.validated_data)
        user.set_password(password)
        user.save()
        if user.is_student:
            Student.objects.create(user=user)
            return Response(self.get_serializer(user).data,status=status.HTTP_201_CREATED)
        if user.is_teacher:
            Teacher.objects.create(user=user)
        return Response(self.get_serializer(user).data,status=status.HTTP_201_CREATED)








