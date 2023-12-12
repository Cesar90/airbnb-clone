from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):
class CustomUserAdmin(UserAdmin):
    """
        Custom User Admin
    """
    # list_display = ('username','email','gender', 'language', 'superhost')
    # list_filter = ('language','currency','superhost',)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profiles",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost"
                )
            }
        ),
    )

# admin.site.register(models.User, CustomUserAdmin)