# Generated by Django 5.0.1 on 2024-02-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_realtor_stars_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
