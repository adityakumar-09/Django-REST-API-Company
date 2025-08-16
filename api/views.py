from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializer
# Create your views here.
# we will not function based view. Django REST framework give better way

class CompanyViewSet(viewsets.ModelViewSet): # this ModelViewSet provide defualt methods
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

