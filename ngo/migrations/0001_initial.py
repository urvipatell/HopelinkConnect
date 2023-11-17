# Generated by Django 4.2.1 on 2023-09-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phoneNumber', models.IntegerField()),
                ('dob', models.DateTimeField()),
                ('email', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='Media/UserImage/%Y/')),
                ('username', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
            ],
        ),
    ]
