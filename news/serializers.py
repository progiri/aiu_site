from .models import News
from rest_framework.serializers import ModelSerializer


class NewsSerializer(ModelSerializer):

	class Meta:
		model = News
		fields = '__all__'
