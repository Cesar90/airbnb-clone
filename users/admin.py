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

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        # "email_verified",
        # "email_secret",
        # "login_method",
    )


# admin.site.register(models.User, CustomUserAdmin)