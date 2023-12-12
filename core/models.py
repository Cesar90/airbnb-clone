from django.db import models

class TimeStampedModel(models.Model):
    """
        Time Stamped Model
    """
    created = models.DateField()
    updated = models.DateField()

    # This model doesn't go to database
    class Meta:
        abstract: True
