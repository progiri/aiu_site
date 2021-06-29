from .serializers import CompanySerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from .models import Company


# Create your views here.
class CompaniesViews(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
