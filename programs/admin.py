from django.contrib import admin

from .models import Television, Program, UserPrograms

# Register your models here.

admin.site.register(Television)
admin.site.register(Program)
admin.site.register(UserPrograms)
