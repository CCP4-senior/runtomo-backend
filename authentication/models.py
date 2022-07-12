# from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, image, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))

        if not email:
            pass

        email=self.normalize_email(email)

        new_user=self.model(email=email, image = image, **extra_fields)

        new_user.set_password(password)

        new_user.save()

        return new_user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff flagged as True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser flagged as True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active flagged as True"))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    image = models.CharField(max_length=300, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()


    def __str__(self):
        return f"<User {self.email}"