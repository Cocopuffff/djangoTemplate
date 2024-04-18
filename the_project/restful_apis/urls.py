from django.urls import path
from . import views

urlpatterns = [
    path('task-list/', views.TaskList.as_view()),
    path('task-details/<str:pk>/', views.TaskDetails.as_view()),
    path('task-create/', views.TaskCreate.as_view()),
    path('task-update/<str:pk>/', views.TaskUpdate.as_view()),
    path('task-delete/<str:pk>/', views.TaskDelete.as_view())
]