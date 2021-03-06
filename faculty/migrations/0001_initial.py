# Generated by Django 3.2 on 2021-04-24 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Степень')),
            ],
            options={
                'verbose_name': 'Степень',
                'verbose_name_plural': 'Сетепени',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=2500, verbose_name='Описание')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultys', to='faculty.degree')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
    ]
