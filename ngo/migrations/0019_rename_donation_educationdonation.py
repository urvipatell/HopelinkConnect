# Generated by Django 4.2.1 on 2023-10-09 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0018_donation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Donation',
            new_name='EducationDonation',
        ),
    ]