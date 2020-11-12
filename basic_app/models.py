from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustUser(AbstractUser):
    #Total Fields : 3
    #Total Roles : 3
    #------Custom User Table Fields------
    '''Overrides the custom django user model'''
    # Datafields
    SUPER_ADMIN = 1
    ADMIN = 2
    NORMAL_USER = 3
    ROLE_CHOICES = (  
      (SUPER_ADMIN,'super_admin'),
      (ADMIN,'admin'),
      (NORMAL_USER,'normal_user'),
    )
    #This field store User's Role
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=NORMAL_USER)  