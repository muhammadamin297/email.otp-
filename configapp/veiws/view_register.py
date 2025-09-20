import random
from django.contrib.auth.hashers import make_password
from configapp.Permission import IsEmailVerified
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from configapp.serializers import SendEmail,VerifySerializer,UserSerializer
class SendEmailAPI(APIView):
    @swagger_auto_schema(request_body=SendEmail)
    def post(self,request):
        serializer = SendEmail(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = "Registiratsiya kod"
        message = str(random.randint(100000, 999999))
        email = serializer.validated_data['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [f"{email}"]
        if message:
            cache.set(email,message,600)
            send_mail(subject,message,email_from,recipient_list)
        return Response(data={f"{email}":"Yuborildi"})

class VerifyApi(APIView):
    @swagger_auto_schema(request_body=VerifySerializer)
    def post(self,request):
        serializer = VerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        verify_kod = serializer.validated_data['verify_kod']
        cache_cod = str(cache.get(email))
        if verify_kod == cache_cod:
            cache.set(f"{email}_verified", True, 600)
            return Response({
                'status': True,
                'detail': 'OTP matched'
            })
        else:
            return Response({
                'status': False,
                'detail': 'In Correct'
            })
class RegisterApi(APIView):
    permission_classes = [IsEmailVerified]
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data["password"]
        serializer.validated_data["password"] = make_password(password)
        serializer.save()
        return Response({
            'status':True,
            'detail':'Account create'
        })


