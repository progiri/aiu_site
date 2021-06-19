from django.db import models


# Create your models here.
class News(models.Model):
    """ Модель урока """
    title = models.CharField(
    	max_length=255,
        verbose_name='Название новости')
    text = models.TextField(verbose_name='Текст новости')
    pub_date = models.DateTimeField(
    	auto_now_add=True,
        null=True, blank=True,
        verbose_name='Дата и время создание новости')
    edited_date_time = models.DateTimeField(
    	auto_now=True,
        null=True, blank=True,
        verbose_name='Дата и время изменения новости')
    image = models.ImageField(
    	upload_to='news_images/',
        null=True, blank=True,
        verbose_name='Фото')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Category(models.Model):
	title = models.CharField(
		max_length=255,
		verbose_name='Название категория')
	slug = models.SlugField(
		max_length=55,
		verbose_name='Ссылка')
	
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.title


class Tag(models.Model):
	title = models.CharField(
		max_length=255,
		verbose_name='Название тега')
	slug = models.SlugField(
		max_length=255,
		verbose_name='Ссылка')

	class Meta:
		verbose_name = 'Тег'
		verbose_name_plural = 'Теги'

	def __str__(self):
		return self.title
