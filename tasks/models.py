from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    done = models.BooleanField()
    # Many-to-many
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    class Meta:
        ordering = ("done", "datetime",)

    def __str__(self):
        return f"{self.content} (created: {self.datetime}, done status: {self.done})"

    def get_absolute_url(self):
        return reverse("tasks:task-detail", args=[str(self.id)])
