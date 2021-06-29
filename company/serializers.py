from django.contrib.auth import models
from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from .models import Company, Location, Position


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = ('title',)


class PositionSerializer(ModelSerializer):

    class Meta:
        model = Position
        fields = ('title',)


class CompanySerializer(ModelSerializer):
    position = PositionSerializer()
    location = LocationSerializer()

    class Meta:
        model = Company
        fields = ('title', 'description', 'position', 'location')

