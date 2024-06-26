# Generated by Django 5.0.4 on 2024-04-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container_announcements', '0003_city_name_en_city_name_ru_city_name_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerprovider',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='containerprovider',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='containerprovider',
            name='description_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='containerprovider',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='containerprovider',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='containerprovider',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
    ]
