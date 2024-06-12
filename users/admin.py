from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    """
    Custom user admin, it customizes the user admin panel
    look
    """

    # form used by admin to add a new user
    add_form = CustomUserCreationForm
    # form used by admin to update user info
    form = CustomUserChangeForm
    # model to be used by this user admin panel section not the whole admin dashboard
    model = CustomUser

    # sample fields to be display when viewing all users
    list_display = ["username", "is_active", "is_staff", "is_superuser"]
    list_filter = ["username", "is_active", "is_staff"]

    # fields and permissions to be rendered when updating user info using the admin panel
    fieldsets = [
        (None, {"fields": ("username", "password")}),
        (
            "Permission",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    ]
    # fields and permissions to be rendered when creating a user using the admin panel
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "username",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ],
            },
        )
    ]
    # fields used for searching in users
    search_fields = ["username"]
    ordering = ["username"]


# make the CustomUser model use the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
