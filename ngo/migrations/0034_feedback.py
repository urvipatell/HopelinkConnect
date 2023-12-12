# Generated by Django 4.2.1 on 2023-12-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0033_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('feedback_type', models.CharField(max_length=20)),
                ('comments', models.TextField()),
            ],
        ),
    ]