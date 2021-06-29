from django.db.models import query
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView

from .serializers import NewsSerializer
from .models import News
from user.permissions import IsAdmin

class NewsListView(ListAPIView):

    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsCRUDView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

