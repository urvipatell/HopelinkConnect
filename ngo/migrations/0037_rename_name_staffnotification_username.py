# Generated by Django 4.2.1 on 2023-12-10 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0036_staffnotification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffnotification',
            old_name='name',
            new_name='username',
        ),
    ]