import logging
import typing as t

from django.utils import timezone

from tasks import models

logger = logging.getLogger(__name__)


def complete_task(task: models.Task) -> models.Task:
    task.completed_last_date = timezone.now().date()
    task.save()
    task.refresh_from_db()
    return task
