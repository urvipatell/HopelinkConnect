# Generated by Django 4.2.1 on 2023-12-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0038_alter_staffnotification_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event_datetime', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]
