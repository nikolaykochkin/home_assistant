from django.shortcuts import render
from django.views import generic
from .models import Task


class TaskList(generic.ListView):
    template_name = 'scheduler/index.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        return Task.objects.all()

class TaskView(generic.ListView):
    template_name = 'scheduler/task.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.all()
