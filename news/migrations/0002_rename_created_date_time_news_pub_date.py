# Generated by Django 3.2.4 on 2021-06-28 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='created_date_time',
            new_name='pub_date',
        ),
    ]
