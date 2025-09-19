from rest_framework.routers import DefaultRouter
from configapp.veiws import *
from django.urls import path,include
router = DefaultRouter()
router.register(r'teachers',TeacherCreateApi)

urlpatterns = [
    path('',include(router.urls)),
    path('send_mail/',SendEmailAPI.as_view(),name = 'send_email')
]