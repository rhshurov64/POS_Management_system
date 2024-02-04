from rest_framework import serializers
from .models import *

from base.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'school', 'address']
        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'code', 'description', 'image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'code', 'size', 'price', 'quantity', 'description', 'categories', 'image']