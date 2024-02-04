from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import StudentSerializer, ProductSerializer, CategorySerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
# Create your views here.

from restapi.serializers import *


@csrf_exempt
@api_view(['GET', 'POST','PUT', 'PATCH', 'DELETE'])
def student_api(request, id = None):
    if request.method == "GET":
        if id is not None:
            student = Student.objects.get(id =id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
    if request.method == 'DELETE':
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == "PUT":
        student = Student.objects.get(id =id)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
    if request.method == "PATCH":
        student = Student.objects.get(id =id)
        serializer = StudentSerializer(student, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)


class class_api(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        student = Student.objects.get(pk =pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        student = Student.objects.get(pk =pk)
        serializer = StudentSerializer(student, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
            snippet = self.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        


class StudentModelViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    permission_classes = [IsAdminUser]
    authentication_classes = [BasicAuthentication]
    
    
class CategoryModelViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [BasicAuthentication]
    
class ProductModelViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [BasicAuthentication]
    
