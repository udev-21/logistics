# Generated by Django 5.0.4 on 2024-07-15 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_services', '0004_logisticsservice_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logisticsservice',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='logisticsservice',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='logisticsservicetype',
            name='name_en',
        ),
    ]