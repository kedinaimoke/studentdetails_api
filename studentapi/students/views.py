from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serializers import StudentSerializers


@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all student names and other details that follow.
    """
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
