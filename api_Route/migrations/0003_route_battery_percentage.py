# Generated by Django 4.2.4 on 2023-09-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_Route', '0002_alter_route_latitude_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='battery_percentage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
