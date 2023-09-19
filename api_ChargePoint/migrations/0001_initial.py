# Generated by Django 4.2.4 on 2023-09-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChargePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_point', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created_at_point', models.DateTimeField(auto_now_add=True)),
                ('updated_at_point', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]