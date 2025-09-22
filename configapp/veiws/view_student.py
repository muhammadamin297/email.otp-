from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from configapp.Permission import IsEmailVerified,IsAdmin
from configapp.models import *
from configapp.serializers import StudentSerializer, UserSerializer, StudentAndUserSerializer, ChangePasswordSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
class StudentDetailApi(ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [IsEmailVerified, IsAdmin]
    def get_permissions(self):
        if self.action in ["list", "retrieve", "update", "destroy"]:
            return [IsAdmin()]
        return [IsEmailVerified(), IsAdmin()]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "update", "destroy"]:
            return StudentSerializer
        return StudentAndUserSerializer

    def create(self,request,*args,**kwargs):
        user_data = request.data.get('user',None)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save(is_student=True, must_change_password=True, is_active=True)
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

@swagger_auto_schema(method="post",request_body=ChangePasswordSerializer)
@api_view(['POST'])
def change_password(request):
    new_password = request.data.get("new_password")
    if not new_password:
        return Response({"detail":"Password invalid!"}, status=400)
    user = request.user
    user.set_password(new_password)
    user.is_active = True
    user.save()
    return Response({"detail":"Password changed successfully"})

class LoginApi(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        return Response({
            "id": user.id,
            "email": user.email,
            "detail": "Login muvaffaqiyatli bajarildi"
        }, status=status.HTTP_200_OK)
