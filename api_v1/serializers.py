from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField
from .models import Task, Tag



class TagListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='tag_detail_url',
        lookup_field='id'
    )
    class Meta:
        model = Tag
        fields = (
            'name',
            'date',
            'url'
        )

class TaskOfTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'date',
        )

class TagDetailSerializer(serializers.ModelSerializer):
    tasks = SerializerMethodField()
    class Meta:
        model = Tag
        fields = ('id','name','date','tasks')
    
    def get_tasks(self, obj):
        if obj.tasks:
            return TaskOfTagSerializer(obj.tasks, many=True).data
        return 0

class TagOfTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
            'date',
        )

class TaskDetailSerializer(serializers.ModelSerializer):
    tags = SerializerMethodField()
    class Meta:
        model = Task
        fields = ('id','name','description','date','tags')
    
    def get_tags(self, obj):
        if obj.tags:
            return TagOfTaskSerializer(obj.tags, many=True).data
        return 0

class TaskListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'task_detail_url',
        lookup_field = 'id'
    )
    tags = SerializerMethodField()
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'date',
            'url',
            'tags',
        )
    
    def get_tags(self, obj):
        return obj.tags.count()

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name','description','tags')

class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name','tasks')


