from rest_framework.fields import ChoiceField
from rest_framework.serializers import ModelSerializer
from .models import Faculty, SpecialDirection

class FacultySerializer(ModelSerializer):

    DEGREE_CHOICES = [
		('B', 'Bachelor'),
		('M', 'Master'),
		('D', 'Doctor')
	]

    degree = ChoiceField(DEGREE_CHOICES)

    class Meta:
        model = Faculty
        fields = ('title', 'description', 'image', 'price', 'degree')


class SpecialDirectionSerializer(ModelSerializer):

    faculty = FacultySerializer()

    class Meta:
        model = SpecialDirection
        fields = ('title', 'description', 'image', 'faculty')
