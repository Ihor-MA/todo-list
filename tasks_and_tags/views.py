from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Tag, Task


class TagListView(generic.ListView):
    model = Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.order_by("is_task_done", "deadline")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks_and_tags:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks_and_tags:tag-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks_and_tags:task-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks_and_tags:tag-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks_and_tags:task-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks_and_tags:tag-list")
