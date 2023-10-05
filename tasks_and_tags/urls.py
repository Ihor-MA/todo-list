from django.urls import path

from .views import TagListView

urlpatterns = [
    # path("", homepage, name="homepage"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "tasks_and_tags"
