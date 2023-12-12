from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """
        Custom User Admin
    """
    list_display = ('username','email','gender', 'language', 'superhost')
    list_filter = ('language','currency','superhost',)

# admin.site.register(models.User, CustomUserAdmin)