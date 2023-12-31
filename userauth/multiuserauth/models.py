from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, usename, password, **extra_fields):
        if not usename:
            raise ValueError(_('The usename must be set'))
        user = self.model(username=usename, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('user_type', 'admin')
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)




USER_TYPE_COICES = (('agent','Agent'),
                    ('admin','Admin'),
                    ('customers','Customers'))


class User(AbstractUser):
    user_type = models.CharField(choices=USER_TYPE_COICES,max_length=50)
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,null=True,blank=True)
    is_staff = models.BooleanField(default=True,null=True,blank=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    last_login = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()


class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_agent')
    name = models.CharField(max_length=120)
    address = models.TextField()


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_customer')
    name = models.CharField(max_length=120)
    address = models.TextField()