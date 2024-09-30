from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from library2_0 import settings

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    username = None         # remove username fields from default user model
    email = models.EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", null=True, blank=True)
    mobile = models.PositiveBigIntegerField(null=True, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.email
