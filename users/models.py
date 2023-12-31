import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string

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

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"), 
        (LOGIN_GITHUB, "Github"), 
        (LOGIN_KAKAO, "Kakao"),
    )

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
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)

    # def __str__(self) -> str:
    #     return super().__str__()

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            # html_message = f'To verify your account click <a href="http://127.0.0.1:8000/users/verify/{secret}">here</a>'
            html_message = render_to_string(
                "emails/verify_email.html", {'secret':secret}
            )
            send_mail(
                "Verify Airbnb Account", 
                strip_tags(html_message), 
                settings.EMAIL_FROM, 
                [self.email],
                fail_silently=True,
                html_message=html_message
            )
            self.save()
        return