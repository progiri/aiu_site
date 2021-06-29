# Generated by Django 3.2.4 on 2021-06-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_auto_20210619_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='facultys/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена за обучение(год)'),
        ),
    ]