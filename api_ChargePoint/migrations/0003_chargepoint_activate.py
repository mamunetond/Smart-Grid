# Generated by Django 4.2.4 on 2023-09-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_ChargePoint', '0002_chargepoint_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargepoint',
            name='activate',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
