from .models import Task, Tag
from .pagination import MyPageNumberPagination

from .serializers import (
    TaskListSerializer,
    TaskDetailSerializer,
    TagDetailSerializer,
    TagListSerializer,
    TaskCreateSerializer,
    TagCreateSerializer
)

from rest_framework.generics import (
   ListAPIView, 
   RetrieveAPIView, 
   UpdateAPIView, 
   DestroyAPIView, 
   CreateAPIView,
   RetrieveUpdateAPIView
)


class TaskListAPIView(ListAPIView): 
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    pagination_class = MyPageNumberPagination

    #def get_queryset()

class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    lookup_field = 'id'

class TagDetailAPIView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    lookup_field = 'id'

class TagListAPIView(ListAPIView): 
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    pagination_class = MyPageNumberPagination

    #def get_queryset()

class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

class TagCreateAPIView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCreateSerializer


