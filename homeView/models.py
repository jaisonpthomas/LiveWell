from django.db import models
from datetime import date


# Create your models here.
class HealthData(models.Model):
    dateVal = models.DateField(default=date.today, unique=True)
    score = models.IntegerField(blank=True, null=True)
    symptoms = models.TextField(default="", blank=True)
    relevantFactors = models.TextField(default="", blank=True)

    def __str__(self):
        return str(self.dateVal) + ": " + str(self.score)
