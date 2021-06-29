from django.db import models


class Location(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Местоположение (город)'
        verbose_name_plural = 'Местоположения (город)'
    
    def __str__(self) -> str:
        return self.title


class Position(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
    
    def __str__(self) -> str:
        return self.title



class Company(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=2555,
        verbose_name='Описание'
    )
    location = models.ForeignKey(
        to=Location,
        on_delete=models.SET_NULL,
        related_name='companies',
        null=True, blank=True,
        verbose_name='Местоположение (город)'
    )
    position = models.ForeignKey(
        to=Position,
        on_delete=models.SET_NULL,
        related_name='companies',
        null=True, blank=True,
        verbose_name='Должность'
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
    
    def __str__(self) -> str:
        return self.title


