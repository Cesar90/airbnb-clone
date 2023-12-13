from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Review)
class Review(admin.ModelAdmin):
    """
        Review Admin Definition
    """
    pass