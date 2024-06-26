# Generated by Django 5.0.4 on 2024-04-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container_announcements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Shipping Type',
                'verbose_name_plural': 'Shipping Types',
                'db_table': 'shipping_types',
                'ordering': ['id', 'created_at'],
            },
        ),
    ]
