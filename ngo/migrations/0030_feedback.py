# Generated by Django 4.2.1 on 2023-12-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0029_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='user_images/')),
                ('feedback_type', models.CharField(choices=[('compliment', 'Compliment'), ('suggestion', 'Suggestion'), ('thought', 'thought')], max_length=20)),
                ('comments', models.TextField()),
            ],
        ),
    ]
