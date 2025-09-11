from django.urls import path,include
from rest_framework.routers import DefaultRouter
from configapp.veiws import *
router = DefaultRouter()
router.register(r'user',UserApi)
router.register(r'student',StudentApi)

urlpatterns = [
    path('',include(router.urls)),
]