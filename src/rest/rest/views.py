from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
#from pymongo import MongoClient
from serializers import TaskSerializer
#mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
#db = MongoClient(mongo_uri)['test_db']

@api_view(['GET'])
def view_items(request):
    task = TaskSerializer(data=request.data)

    if Task.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(task.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
@api_view(['POST'])
def add_items(request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
    if request.query_params:
        items = Task.objects.filter(**request.query_param.dict())
    else:
        items = Task.objects.all()
  
   
    if items:
        data = TaskSerializer(items)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

