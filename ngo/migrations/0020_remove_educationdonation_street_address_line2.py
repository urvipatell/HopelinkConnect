# Generated by Django 4.2.1 on 2023-10-09 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0019_rename_donation_educationdonation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationdonation',
            name='street_address_line2',
        ),
    ]