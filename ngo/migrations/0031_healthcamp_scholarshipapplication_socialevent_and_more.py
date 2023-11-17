# Generated by Django 4.2.1 on 2023-10-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0030_remove_fooddonation_address_remove_fooddonation_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofdoctor', models.CharField(max_length=255)),
                ('nameoforg', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumberarea', models.CharField(blank=True, max_length=10, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=10, null=True)),
                ('types1', models.CharField(blank=True, max_length=255, null=True)),
                ('types2', models.CharField(blank=True, max_length=255, null=True)),
                ('types3', models.CharField(blank=True, max_length=255, null=True)),
                ('types4', models.CharField(blank=True, max_length=255, null=True)),
                ('types5', models.CharField(blank=True, max_length=255, null=True)),
                ('timeinput', models.CharField(blank=True, max_length=8, null=True)),
                ('ampm', models.CharField(blank=True, max_length=2, null=True)),
                ('datemonth', models.CharField(blank=True, max_length=2, null=True)),
                ('dateday', models.CharField(blank=True, max_length=2, null=True)),
                ('dateyear', models.CharField(blank=True, max_length=4, null=True)),
                ('addrline1', models.CharField(max_length=255)),
                ('addresscity', models.CharField(max_length=255)),
                ('addressstate', models.CharField(max_length=255)),
                ('addresspostal', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScholarshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('nameoforg', models.CharField(blank=True, max_length=255, null=True)),
                ('nameofscholarship', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('area', models.CharField(blank=True, max_length=10, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=10, null=True)),
                ('typeofscholarship', models.CharField(max_length=255)),
                ('datemonth', models.CharField(max_length=2)),
                ('dateday', models.CharField(max_length=2)),
                ('dateyear', models.CharField(max_length=4)),
                ('addrline1', models.CharField(max_length=255)),
                ('addresscity', models.CharField(max_length=255)),
                ('addresstate', models.CharField(max_length=255)),
                ('addresspostal', models.CharField(max_length=10)),
                ('benefit', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('type_of_event', models.CharField(max_length=255)),
                ('activity_time', models.TimeField()),
                ('activity_date', models.DateField()),
                ('address_line1', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('file_upload', models.FileField(upload_to='uploads/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('story_name', models.CharField(max_length=255)),
                ('user_story', models.TextField()),
                ('notes', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
