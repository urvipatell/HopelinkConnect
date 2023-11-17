# Generated by Django 4.2.1 on 2023-10-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0028_rename_notes_clothdonation_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('organization_name', models.CharField(max_length=255)),
                ('organization_mission', models.TextField()),
                ('date_needed', models.DateField()),
                ('time_needed', models.TimeField()),
                ('pickup_address', models.CharField(max_length=255)),
                ('pickup_city', models.CharField(max_length=100)),
                ('pickup_state', models.CharField(max_length=100)),
                ('pickup_postal_code', models.CharField(max_length=20)),
            ],
        ),
    ]