from django.utils.translation import get_language
from user.permissions import IsAdmin
from .serializers import FacultySerializer
from .models import ApplicationForDirection, Faculty, SpecialDirection
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response

# Create your views here.

class FacultiesView(generics.ListAPIView):
    
    permission_classes = [permissions.AllowAny]
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyCreateAPIView(generics.ListCreateAPIView):

    permission_classes = [IsAdmin]
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class SpecialDirectionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        return SpecialDirection.objects.filter(faculty=self.request.user.profile)

class RequestToDirection(generics.GenericAPIView):

    def get(self, request):
        
        directions = SpecialDirection.objects.filter(faculty=request.user.profile.faculty)
        return Response(directions.values())

    def post(self, request):
        direction_id = request.data['direction_id']
        comment = request.data['comment']

        user = request.user

        direction = ApplicationForDirection.objects.create(
            user=user,
            direction=SpecialDirection.objects.get(id=direction_id), 
            comment=comment
        )
        print(direction)

        return Response({
            "user": direction.user.email,
            "direction": direction.direction.title,
            "comment": direction.comment
        })

