from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User





class Department(models.Model):
    dept_name = models.CharField(max_length=100,null=True)

class Service(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    service_name = models.CharField(max_length=200,null=True)



class CustomUser(AbstractUser):
    user_type = models.CharField(default='1',max_length=10)



    

