# Generated by Django 3.1.3 on 2020-11-24 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_auto_20201124_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='datetime',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default='2021-08-14'),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default='19:30'),
        ),
    ]
