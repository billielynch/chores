from datetime import date

from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Task(models.Model):
    name: models.CharField = models.CharField(blank=False, unique=True, max_length=120)
    completed_last_date: models.DateField = models.DateField(blank=True, null=True)
    frequency_days: models.PositiveIntegerField = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(1)]
    )

    def get_absolute_url(self):
        return reverse("task-list")

    def __str__(self):
        return f"{self.name} : {self.completed_last}"

    NOT_COMPLETED_VALUE = "never"

    @property
    def completed_last(self):
        if self.completed_last_date:
            return self.completed_last_date.isoformat()

        return self.NOT_COMPLETED_VALUE

    @property
    def due(self):
        if not self.completed_last_date:
            return True
        difference = now().date() - self.completed_last_date
        return True if difference.days > self.frequency_days else False
