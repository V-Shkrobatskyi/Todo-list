from django.urls import path
from tasks.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TaskChangeStatusView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/change-status/", TaskChangeStatusView.as_view(), name="task-change-status"),
]

app_name = "tasks"
