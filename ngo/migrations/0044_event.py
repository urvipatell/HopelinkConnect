# Generated by Django 4.2.1 on 2023-11-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0043_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(choices=[('Social Activity', 'Social Activity'), ('Impact Story', 'Impact Story'), ('Health Camp', 'Health Camp'), ('Scholarship', 'Scholarship')], max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]