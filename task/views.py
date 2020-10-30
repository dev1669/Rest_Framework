from django.shortcuts import render
from .models import Employee
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import EmployeeSerializer

# Create your views here.
def home(request):
    return render(request,'home.html')


@api_view(['GET','POST','PUT','DELETE'])
def api_access(request,pk):
    try:
        table_data = Employee.objects.get(emp_id=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(table_data)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'data is created successfully'             
            return Response(data=data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(table_data,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'data is updated successfully....'          
            return Response(data=data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        data = {}
        table_data.delete()
        data['success'] = 'data is deleted successfully...'
        return Response(data=data)