# Generated by Django 3.2.4 on 2021-06-28 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_alter_studentsubject_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Информация')),
                ('postiton', models.CharField(max_length=255, verbose_name='Должность')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_info', to=settings.AUTH_USER_MODEL, verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Информация о преподавателе',
                'verbose_name_plural': 'Информации о преподавателях',
            },
        ),
    ]