# Generated by Django 4.2.1 on 2023-10-09 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0020_remove_educationdonation_street_address_line2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educationdonation',
            old_name='street_address',
            new_name='address',
        ),
    ]
