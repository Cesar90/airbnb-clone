import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail

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
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    # def __str__(self) -> str:
    #     return super().__str__()

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail(
                "Verify Airbnb Account", 
                f"Verify Account, this is your secre: {secret}", 
                settings.EMAIL_FROM, 
                [self.email],
                fail_silently=True)
        return