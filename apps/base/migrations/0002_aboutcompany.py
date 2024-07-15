# Generated by Django 5.0.4 on 2024-07-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('desc', models.TextField(verbose_name='description')),
                ('image', models.ImageField(default='/about_company/default.png', upload_to='about_company')),
                ('phone', models.CharField(max_length=20)),
                ('telegram_link', models.URLField(blank=True, null=True)),
                ('whatsapp_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]