# Generated by Django 5.0.1 on 2024-01-31 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_extrainformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainformation',
            name='rate',
            field=models.PositiveIntegerField(),
        ),
    ]
