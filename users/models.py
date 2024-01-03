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

    avatar = models.ImageField(upload_to="avatars",blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGES_CHOICES, 
        max_length=2,blank=True, 
        default=LANGUAGE_SPANISH)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, 
        max_length=3,blank=True, 
        default=CURRENCY_NIC)
    superhost = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    # def __str__(self) -> str:
    #     return super().__str__()

    def verify_email(self):
        pass