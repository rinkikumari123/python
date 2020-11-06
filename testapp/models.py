from django.db import models
from django.contrib.auth.models import AbstractUser

'''
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
'''
class Student(models.Model):
    name =models.CharField(max_length=30)
    marks=models.FloatField()
    roll_num =models.FloatField()
    created_date=models.DateTimeField(auto_now_add=True, null=True)
    city = models.CharField(max_length=30 ,null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    updated_By = models.CharField(max_length=30 ,null=True)

    def __str__(self):
        return self.name


class AdminRegistraion(models.Model):
    name = models.CharField(max_length=30)
    phone_no = models.IntegerField()
    email_id = models.EmailField(max_length= 30,unique=True)
    city = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()
