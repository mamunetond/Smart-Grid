# Generated by Django 4.2.4 on 2023-10-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_chargepoint_user_electricvehicle_user_route_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargepoint',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
