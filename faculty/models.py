from django.db import models
from django.contrib.auth import get_user_model


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
	image = models.ImageField(
		upload_to='faculty_info_img/',
		null=True, blank=True,
		verbose_name='Фото'
	)
	price = models.IntegerField(
		null=True, blank=True,
		verbose_name='Цена за обучение(год)'
	)
	degree = models.CharField(
		max_length=1,
		choices=DEGREE_CHOICES)

	class Meta:
		verbose_name = 'Факультет'
		verbose_name_plural = 'Факультеты'

	def __str__(self) -> str:
		return self.title


class SpecialDirection(models.Model):
	title = models.CharField(
		max_length=255,
		verbose_name='Название'
	)
	description = models.CharField(
		max_length=2555,
		verbose_name='Описание'
	)
	image = models.ImageField(
		upload_to='special_directions/',
		null=True, blank=True,
		verbose_name='Фото'
	)
	faculty = models.ForeignKey(
		to=Faculty,
		on_delete=models.CASCADE,
		null=True, blank=True,
		related_name='directions',
		verbose_name='Факультет'
	)

	class Meta:
		verbose_name = 'Направление по специальности'
		verbose_name_plural = 'Направлении по специальностям'

	def __str__(self) -> str:
		return f"Направление {self.title} в факультете {self.faculty}"


class ApplicationForDirection(models.Model):
	user = models.OneToOneField(
		to=get_user_model(),
		on_delete=models.CASCADE,
		related_name='application_for_direction',
		verbose_name='Пользователь'
	)
	direction = models.OneToOneField(
		to=SpecialDirection,
		on_delete=models.CASCADE,
		related_name='application_for_direction',
		verbose_name='Направление'
	)
	comment = models.CharField(
		max_length=2555,
		verbose_name='Комментарий'
	)

	class Meta:
		verbose_name = 'Заявка на направление'
		verbose_name_plural = 'Заявки на направления'

	def __str__(self) -> str:
		return f"Заявка от студента {self.user} на направление {self.direction}"
