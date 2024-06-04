# Generated by Django 5.0.4 on 2024-06-04 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('container_announcements', '0007_containerprovider_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerannouncement',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='container_announcements_from_city', to='base.currency'),
        ),
        migrations.AddField(
            model_name='containerannouncement',
            name='is_by_agreement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='containerannouncement',
            name='price',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
