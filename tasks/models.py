from django.db import models
from django.urls import reverse


class Task(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=120)
    completed_last = models.DateField(blank=True, null=True)
    # frequency_days = models.PositiveIntegerField() need to make not equal to zero?

    def get_absolute_url(self):
        return reverse("task-list")

    def __str__(self):
        return f"{self.name} : {self.completed_last.isoformat()}"
