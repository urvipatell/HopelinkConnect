# Generated by Django 4.2.1 on 2023-10-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0031_healthcamp_scholarshipapplication_socialevent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddonation',
            name='time_needed',
            field=models.CharField(max_length=255),
        ),
    ]