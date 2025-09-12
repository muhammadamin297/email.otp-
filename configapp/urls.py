from django.urls import path,include
from rest_framework.routers import DefaultRouter
from configapp.veiws import *
router = DefaultRouter()
router.register(r'user',UserApi)

urlpatterns = [
    path('',include(router.urls)),
    path('students/<int:pk>/', StudentDetailApi.as_view(), name='student-detail'),
    path("students/", StudentListApi.as_view(), name="student-list"),
    path('teachers/<int:pk>/', TeacherDetailApi.as_view(), name='teacher-detail'),
    path("teachers/", TeacherListApi.as_view(), name="teacher-list"),
]
