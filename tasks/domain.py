from django.utils import timezone

from tasks import models


def complete_task(task: models.Task) -> models.Task:
    task.completed_last = timezone.now().date()
    task.save()
    task.refresh_from_db()
    return task
