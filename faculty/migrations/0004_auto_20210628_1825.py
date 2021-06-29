# Generated by Django 3.2.4 on 2021-06-28 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faculty', '0003_auto_20210628_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='faculty_info_img/', verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='SpecialDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=2555, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='special_directions/', verbose_name='Фото')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='faculty.faculty', verbose_name='Факультет')),
            ],
            options={
                'verbose_name': 'Направление по специальности',
                'verbose_name_plural': 'Направлении по специальностям',
            },
        ),
        migrations.CreateModel(
            name='ApplicationForDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2555, verbose_name='Комментарий')),
                ('direction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='application_for_direction', to='faculty.specialdirection', verbose_name='Направление')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='application_for_direction', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявка на направление',
                'verbose_name_plural': 'Заявки на направления',
            },
        ),
    ]