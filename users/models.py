from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    """
    This is a custom user model the can be
    instead of the Django User model
    """

    # email field for the use is disenabled
    email = None
    username = models.CharField(_("user name"), max_length=32, unique=True)
    # new field the a custom to the user
    tel = models.IntegerField(_("phone number"), null=True, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    # custom user manager for this custom user
    objects = CustomUserManager()

    def __str__(self):
        return self.username
