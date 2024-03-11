from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from tasks import domain, models


class TaskListView(ListView):
    model = models.Task
    ordering = ["-completed_last"]


class TaskCreateView(CreateView):
    model = models.Task
    fields = ["name"]


class TaskCompleteRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "task-list"

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(models.Task, pk=kwargs["pk"])
        domain.complete_task(task)
        return super().get_redirect_url(*args)
