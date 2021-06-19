from django.db import models

# Create your models here.
class Faculty(models.Model):
	DEGREE_CHOICES = [
		('B', 'Bachelor'),
		('M', 'Master'),
		('D', 'Doctor')
	]

	title = models.CharField(
		max_length=255,
		verbose_name='Название')
	description = models.CharField(
		max_length=2500,
		verbose_name='Описание')
	degree = models.CharField(
		max_length=1,
		choices=DEGREE_CHOICES)

	class Meta:
		verbose_name = 'Факультет'
		verbose_name_plural = 'Факультеты'

	def __str__(self) -> str:
		return self.title




# class Degree(models.Model):
# 	title = models.CharField(
# 		max_length=255,
# 		verbose_name='Степень')

# 	class Meta:
# 		verbose_name = 'Степень'
# 		verbose_name_plural = 'Сетепени'

# 	def __str__(self):
# 		return self.title

