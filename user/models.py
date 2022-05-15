from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin
from django.conf import settings
#from company.models import Company


class UserManager(BaseUserManager):

    def create_user(self,fields):
        """Create and Saves a New User"""
        if not fields['username']:
            raise ValueError('Invalid username')
        username = fields['username']
        del(fields['username'])
        # fields['email'] = fields['email'].lower()
        user = self.model(username=username, **fields)
        try:
         user.set_password(fields['password'])
        except:
            user.set_password(username)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, password=None):
        """Create and Saves Superuser"""
        user = self.create_user({'username': username, 'password': password})
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model that supports Email instead of Username"""
    username = models.CharField(max_length=100, unique=True)
    fullname        = models.CharField(max_length = 30)
    email = models.EmailField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    
