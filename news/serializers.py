from ..models import News, Notification
from rest_framework.serializers import ModelSerializer


class NewsSerializer(ModelSerializer):

	class Meta:
		model = News
		fields = '__all__'


class NotificationSerializer(ModelSerializer):

	class Meta:
		model = Notification
		fields = '__all__'
