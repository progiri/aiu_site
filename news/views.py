from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .serializers import NewsSerializer, NotificationSerializer
from ..models import News, Notification, UserNotifications
from rest_framework.permissions import IsAuthenticated


class NewsView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NotificationsView(ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        # notifications = UserNotifications.objects.filter(user=self.request.user)
        # print(dir(notifications))
        # print(notifications)


        return Notification.objects.order_by('-pub_date')[:5]
