from django.db import models
from .auth_user import User

class Departments(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    descriptions = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField()
    descriptions = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    full_name=models.CharField()
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    departments = models.ManyToManyField(Departments,related_name='get_departament')
    course = models.ManyToManyField(Course,related_name='get_course')
    descriptions = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.full_name