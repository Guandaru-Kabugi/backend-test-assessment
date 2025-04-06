from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

# This is a custom user manager that handles the creation of custom user and superuser accounts.
class UserManager(BaseUserManager):
    def create_user(self,email,username, first_name,last_name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,first_name,last_name,password=None):
        user = self.create_user(email,username,first_name,last_name,password)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user    

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,max_length=255)
    username = models.CharField(max_length=55,unique=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    def __str__(self):
        return self.email