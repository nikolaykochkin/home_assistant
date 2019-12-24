from django.shortcuts import render
from django.views import generic
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm


class TaskList(generic.ListView):
    template_name = 'scheduler/task_list.html'
    context_object_name = 'tasks_list'
    model = Task
    # def get_queryset(self):
    #    return Task.objects.all()


class TaskUpdateView(generic.UpdateView):
    template_name = 'scheduler/task_form.html'
    model = Task
    form_class = TaskUpdateForm


class TaskCreateView(generic.CreateView):
    template_name = 'scheduler/task_form.html'
    model = Task
    form_class = TaskCreateForm
