from django.db import models

class TimeStampedModel(models.Model):
    """
        Time Stamped Model
    """
    created = models.DateField(auto_now_add=True) #Get the time and date when new model is created
    updated = models.DateField(auto_now=True) #Get the time and date when the models is updated

    # This model doesn't go to database
    class Meta:
        abstract: True
