# Generated by Django 4.2.1 on 2023-12-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0014_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('countrycode', models.CharField(max_length=4)),
                ('phonenumber', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='user_images/')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('forwhom', models.CharField(choices=[('u', 'User'), ('s', 'Staff')], max_length=1)),
            ],
        ),
    ]
