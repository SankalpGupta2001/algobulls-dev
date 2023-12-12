from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html') 



#GET API TO FETCH ALL TASK 
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_Task(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({
        'status': 200,
        'data': serializer.data
    })


#POST API TO SAVE DATA 

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def save_Task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        tags_str = request.data.get('tags', '')
        tags_list = list(set(tag.strip() for tag in tags_str.split(','))) if tags_str else []
        tags_joined = ','.join(tags_list)
        
        new_task = serializer.save(tags=tags_joined)

        similar_tasks = Task.objects.filter(tags=tags_joined).exclude(id=new_task.id)
        for task in similar_tasks:
            task.tags = tags_joined
            task.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET API TO FETCH ONE TASK
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_By_Id_Task(request, task_id):
    try:
        task_instance = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task_instance)
    return Response(serializer.data)


#PUT API TO UPDATE DATA
@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def update_Task(request, task_id):
    try:
        task_instance = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task_instance, data=request.data)
    if serializer.is_valid():
      
        tags_str = request.data.get('tags', '')
        tags_list = list(set(tag.strip() for tag in tags_str.split(','))) if tags_str else []
        
        tags_joined = ','.join(tags_list)

        serializer.save(tags=tags_joined)

        similar_tasks = Task.objects.filter(tags=tags_joined).exclude(id=task_id)
        for task in similar_tasks:
            task.tags = tags_joined
            task.save()

        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELTE API TO DELETE ONE DATA
@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_Task(request, task_id):
    try:
        task_instance = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    task_instance.delete()
    return Response({'success': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




