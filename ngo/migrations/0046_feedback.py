# Generated by Django 4.2.1 on 2023-11-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0045_rename_event_eventimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('feedback_type', models.CharField(choices=[('compliment', 'Compliment'), ('suggestion', 'Suggestion'), ('issue', 'Issue')], max_length=20)),
                ('comments', models.TextField()),
            ],
        ),
    ]
