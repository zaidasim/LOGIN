from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
=======

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

>>>>>>> another_branch
# Create your models here.
class User(models.Model):
    email=models.EmailField(unique=True)
    text=models.TextField(max_length=200)

<<<<<<< HEAD


=======
>>>>>>> another_branch
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
<<<<<<< HEAD

=======
>>>>>>> another_branch
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
<<<<<<< HEAD
=======
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
>>>>>>> another_branch
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
<<<<<<< HEAD
=======

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
>>>>>>> another_branch
