from django.urls import path

from .views import TagListView, TaskListView, TaskCreateView, TagCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "tasks_and_tags"
