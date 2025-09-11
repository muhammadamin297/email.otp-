from django.db import models
from .auth_user import User
class Teacher(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    user=models.OneToOneField(User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name