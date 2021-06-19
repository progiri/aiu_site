from django.db import models

# Create your models here.
class Subject(models.Model):
	title = models.CharField(
		max_length=255,
		verbose_name='Название')
	discription = models.CharField(
		max_length=2500,
		verbose_name='Описание')

	class Meta:
		verbose_name = 'Предмет'
		verbose_name_plural = 'Предметы'

	def __str__(self):
		return self.title
