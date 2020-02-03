from django.shortcuts import render
from .models import Task


def all(request):
    tasks = Task.objects.all()

    return render(request, "tasks/all.html", {"tasks": tasks, "title": "All"})
