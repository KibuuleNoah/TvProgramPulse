from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user manager to define how the custom user
    will behave e.g how to create a normal user or a superuser
    """

    def create_user(self, username, password, **extra_fields):
        """
        Defines how to create a normal user
        and what fields are needed
        """
        if not username:
            raise ValueError(_("Username must be set"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Defines how to create a super user
        and what fields are needed
        """
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(_("Superuser must have is_staff=True"))
        if not extra_fields.get("is_superuser"):
            raise ValueError(_("Superuser must have is_superuser=True"))
        return self.create_user(username, password, **extra_fields)

    # Add more behavior if needed for this custom user
