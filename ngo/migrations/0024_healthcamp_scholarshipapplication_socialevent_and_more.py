# Generated by Django 4.2.1 on 2023-12-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0023_delete_healthcamp_delete_scholarshipapplication_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formType', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=20)),
                ('nameofdoctor', models.CharField(max_length=255)),
                ('nameoforg', models.CharField(blank=True, max_length=255, null=True)),
                ('types1', models.CharField(blank=True, max_length=255, null=True)),
                ('types2', models.CharField(blank=True, max_length=255, null=True)),
                ('types3', models.CharField(blank=True, max_length=255, null=True)),
                ('types4', models.CharField(blank=True, max_length=255, null=True)),
                ('types5', models.CharField(blank=True, max_length=255, null=True)),
                ('timeinput', models.CharField(blank=True, max_length=8, null=True)),
                ('ampm', models.CharField(blank=True, max_length=2, null=True)),
                ('date', models.CharField(blank=True, max_length=20, null=True)),
                ('addrline1', models.CharField(max_length=255)),
                ('addresscity', models.CharField(max_length=255)),
                ('addressstate', models.CharField(max_length=255)),
                ('addresspostal', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ScholarshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formType', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=20)),
                ('nameoforg', models.CharField(blank=True, max_length=255, null=True)),
                ('nameofscholarship', models.CharField(max_length=255)),
                ('typeofscholarship', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=2)),
                ('addrline1', models.CharField(max_length=255)),
                ('addresscity', models.CharField(max_length=255)),
                ('addresstate', models.CharField(max_length=255)),
                ('addresspostal', models.CharField(max_length=10)),
                ('benefit', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SocialEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formType', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=20)),
                ('type_of_event', models.CharField(max_length=255)),
                ('activity_time', models.CharField(max_length=20)),
                ('activity_date', models.DateField()),
                ('address_line1', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('file_upload', models.FileField(upload_to='socialevent/')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formType', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=20)),
                ('story_name', models.CharField(max_length=255)),
                ('user_story', models.TextField()),
                ('notes', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=255)),
            ],
        ),
    ]
