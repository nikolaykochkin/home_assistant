from django.urls import path
from . import views


app_name = 'scheduler'

urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('task/<int:pk>/', views.TaskUpdateView.as_view(), name='task'),
    path('task/', views.TaskCreateView.as_view(), name='task_form'),
]
