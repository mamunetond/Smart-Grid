# Generated by Django 4.2.4 on 2023-09-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_route_latitude_destination_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargepoint',
            name='company',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
