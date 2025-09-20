from rest_framework.routers import DefaultRouter
from configapp.veiws import *
from django.urls import path,include
router = DefaultRouter()
router.register(r'teachers',TeacherCreateApi)
router.register(r'department',DepartmentAPI)
router.register(r'course',CourseAPI)

urlpatterns = [
    path('',include(router.urls)),
    path('send_mail/',SendEmailAPI.as_view(),name = 'send_email'),
    path('send_sms/',SendEmailAPI.as_view()),
    path('verify/',VerifyApi.as_view()),
    path('register/',RegisterApi.as_view()),
]