# Generated by Django 5.0.4 on 2024-06-04 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['id', 'created_at'],
            },
        ),
    ]
