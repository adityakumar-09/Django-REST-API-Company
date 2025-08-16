from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
# we will not function based view. Django REST framework give better way

class CompanyViewSet(viewsets.ModelViewSet): # this ModelViewSet provide defualt methods
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # companies/{companyId}/employees
    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':"Company might not exists"
            })

class EmployeeViewSet(viewsets.ModelViewSet): # this ModelViewSet provide defualt methods
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer