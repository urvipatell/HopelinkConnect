# Generated by Django 4.2.1 on 2023-10-09 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0026_educationdonation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothdonation',
            old_name='phone_area_code',
            new_name='phone_code',
        ),
        migrations.AddField(
            model_name='clothdonation',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
