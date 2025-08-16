from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer, EmployeeSerializer
# Create your views here.
# we will not function based view. Django REST framework give better way

class CompanyViewSet(viewsets.ModelViewSet): # this ModelViewSet provide defualt methods
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet): # this ModelViewSet provide defualt methods
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer