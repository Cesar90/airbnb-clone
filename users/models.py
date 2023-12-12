from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
        Custom User Model
    """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_SPANISH =  "es"

    LANGUAGES_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_SPANISH, "Spanish"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_NIC = "cor"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_NIC, "COR"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGES_CHOICES, max_length=2,null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3,null=True, blank=True)
    superhost = models.BooleanField(default=False)