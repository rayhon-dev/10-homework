from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('list/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
]