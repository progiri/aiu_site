from django.db import models
from django.contrib.auth import get_user_model
from subject.models import Subject

ADMIN = 'AD'
STUDENT = 'ST'
TEACHER = 'TC'

STATUS_CHOICES = [
    (ADMIN, 'Админ'),
    (STUDENT, 'Ученик'),
    (TEACHER, 'Учитель'),
]


# Create your models here.
class Profile(models.Model):
    """ Профиль пользователя """
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Профиль'
    )
    middle_name = models.CharField(
        max_length=150,
        null=True, blank=True,
        verbose_name='Отчество'
    )
    phone = models.CharField(
        max_length=15,
        null=True, blank=True,
        verbose_name='Номер телефона'
    )
    birth_date = models.DateField(
        null=True, blank=True,
        verbose_name='Дата рождение'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True, blank=True
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        null=True, blank=True
    )
    faculty = models.OneToOneField(
        to='faculty.Faculty',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='users',
        verbose_name='Факультет'
    )
    is_accept = models.BooleanField(
        default=False,
        verbose_name='Подтвержденный'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user)


class StudentSubject(models.Model):
    student = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='subject',
        verbose_name='Студент')
    subject = models.ForeignKey(
        to='subject.Subject',
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='Предмет')

    class Meta:
        verbose_name = 'Предмет студента'
        verbose_name_plural = 'Предметы студентов'

    def __str__(self):
        return f"Предмет {self.subject} студента {self.student.first_name} {self.student.last_name}"


class StaffInfo(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='staff_info',
        verbose_name='Учитель'
    )
    body = models.TextField(
        verbose_name='Информация'
    )
    postiton = models.CharField(
        max_length=255,
        verbose_name='Должность'
    )

    class Meta:
        verbose_name = 'Информация о преподавателе'
        verbose_name_plural = 'Информации о преподавателях'

    def __str__(self) -> str:
        return str(self.user)

