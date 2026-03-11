from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list),
    path('add/', views.add_task),
    path('delete/<int:task_id>/', views.delete_task),
    path('update/<int:task_id>/', views.update_task),  # new URL
]