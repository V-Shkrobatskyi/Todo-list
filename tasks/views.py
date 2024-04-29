# import datetime
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
# from .forms import TaskForm


from .models import Task, Tag
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.count()
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/index.html", context)


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    # form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    # form_class = TaskForm


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tags_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "tasks/tag_confirm_delete.html"
