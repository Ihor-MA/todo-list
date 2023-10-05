from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Tag, Task


class TagListView(generic.ListView):
    model = Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks_and_tags:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks_and_tags:tag-list")
