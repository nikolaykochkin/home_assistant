from django.shortcuts import render
from django.views import generic
from .models import Task


class TaskList(generic.ListView):
    template_name = 'scheduler/index.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        return Task.objects.all()


class TaskView(generic.DetailView):
    template_name = 'scheduler/task.html'
    context_object_name = 'task'
    model = Task


class TaskCreateView(generic.CreateView):
    template_name = 'scheduler/task_form.html'
    model = Task
    fields = ['name', 'executor', 'author', 'description', 'active', 'done', 'start_date',
              'end_date', 'start_time', 'everyday', 'day_of_month']
