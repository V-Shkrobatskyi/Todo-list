from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from .forms import TaskForm

from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"
    queryset = Task.objects.prefetch_related("tags")


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TaskChangeStatusView(View):
    model = Task

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.done = not task.done
        task.save()
        return HttpResponseRedirect(reverse("tasks:task-list"))


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
