from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    path('list/', views.note_list, name='note_list'),
    path('create/', views.note_create, name='note_create'),
    path('detail/<int:pk>/', views.note_detail, name='note_detail'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('update/<int:pk>/', views.note_update, name='note_update'),
]