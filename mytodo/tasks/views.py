from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Task
from .forms import AddTaskForm


def all(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        
        if form.is_valid():
            Task.objects.create(title=form.cleaned_data['input_field']).save()        
            return HttpResponseRedirect('/tasks/all')

    else:
        form = AddTaskForm()

    return render(request, "tasks/all.html", {"form": form,"tasks": tasks, "title_task_list": "All", "count": len(tasks)})


def inbox(request):
    tasks = Task.objects.filter(type_task="inbox")
    return render(request, "tasks/all.html", {"tasks": tasks, "title_task_list": "Inbox", "count": len(tasks)})
