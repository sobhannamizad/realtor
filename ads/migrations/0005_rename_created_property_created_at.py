# Generated by Django 5.0.1 on 2024-02-04 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_property_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='created',
            new_name='created_at',
        ),
    ]
