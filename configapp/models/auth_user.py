from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self,phone_number,password = None,**extra_fields):
        if not phone_number:
            raise ValueError("Phone_number kiritilishi shart")
        user = self.model(phone_number = phone_number,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,phone_number,password,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_staff',True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError("Superuser is_admin = True bo'lishi kerak")
        if extra_fields.setdefault('is_staff') is not True:
            raise ValueError("Superuser is_staff = True bo'lish kerak")

        return self.create_user(phone_number,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r'^\+9989\d{8}$',
        message="telefon raqam tog'ri kelishi kerak"
    )
    phone_number = models.CharField(max_length=13,unique=True)
    sms_kod = models.CharField(max_length=4,null=True,blank=True)
    password = models.CharField()
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    def __str__(self):
        return f"{self.email} - {self.phone_number}"

    @property
    def is_superuser(self):
        return self.is_admin

