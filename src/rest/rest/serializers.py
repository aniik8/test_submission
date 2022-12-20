from django.db.models import fields
from rest_framework import serializers
from .models import Item
  
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('Task')