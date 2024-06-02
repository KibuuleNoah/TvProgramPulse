from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ["username", "is_active", "is_staff", "is_superuser"]
    list_filter = ["username", "is_active", "is_staff"]

    fieldsets = [
        (None, {"fields": ("username", "password")}),
        (
            "Permission",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    ]

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
    search_fields = ["username"]
    ordering = ["username"]


admin.site.register(CustomUser, CustomUserAdmin)
