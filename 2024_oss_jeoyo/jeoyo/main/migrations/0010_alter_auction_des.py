# Generated by Django 3.2.25 on 2024-07-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20240730_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='des',
            field=models.CharField(max_length=255, null=True),
        ),
    ]