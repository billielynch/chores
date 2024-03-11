from django.contrib import admin
from django.urls import path

from tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.TaskListView.as_view(), name="task-list"),
    path("tasks/", views.TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/",
        views.TaskCompleteRedirectView.as_view(),
        name="task-complete",
    ),
]
