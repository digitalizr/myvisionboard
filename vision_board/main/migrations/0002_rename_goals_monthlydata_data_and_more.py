# Generated by Django 4.2.14 on 2024-08-03 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlydata',
            old_name='goals',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='monthlydata',
            name='net_worth',
        ),
        migrations.RemoveField(
            model_name='monthlydata',
            name='weight',
        ),
    ]