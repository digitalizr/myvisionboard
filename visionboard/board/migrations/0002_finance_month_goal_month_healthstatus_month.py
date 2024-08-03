# Generated by Django 4.2.14 on 2024-08-03 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finance',
            name='month',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='goal',
            name='month',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='healthstatus',
            name='month',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
