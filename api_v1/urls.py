from django.urls import path
from .views import (
    TaskListAPIView,
    TaskDetailAPIView,
    TagDetailAPIView,
    TagListAPIView,
    TaskCreateAPIView,
    TagCreateAPIView
)

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='task_list_url'),
    path('tasks/<int:id>/', TaskDetailAPIView.as_view(), name='task_detail_url'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task_create_url'),
    path('tags/<int:id>/', TagDetailAPIView.as_view(), name='tag_detail_url'),
    path('tags/', TagListAPIView.as_view(), name='tag_list_url'),
    path('tags/create/', TagCreateAPIView.as_view(), name='tag_create_url')
]
