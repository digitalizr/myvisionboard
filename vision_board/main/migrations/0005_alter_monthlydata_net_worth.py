# Generated by Django 4.2.14 on 2024-08-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_monthlydata_current_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlydata',
            name='net_worth',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]