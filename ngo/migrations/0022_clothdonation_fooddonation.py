# Generated by Django 4.2.1 on 2023-12-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0021_delete_clothdonation_delete_fooddonation'),
    ]

    operations = [
        migrations.CreateModel(
            name='clothDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formType', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=100)),
                ('type_of_dress', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=20)),
                ('note', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='clothdonation_photos/')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FoodDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formType', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_code', models.CharField(max_length=5)),
                ('phone_number', models.CharField(max_length=20)),
                ('organization_name', models.CharField(max_length=255)),
                ('organization_mission', models.TextField()),
                ('date_needed', models.DateField()),
                ('time_needed', models.CharField(max_length=255)),
                ('pickup_address', models.CharField(max_length=255)),
                ('pickup_city', models.CharField(max_length=100)),
                ('pickup_state', models.CharField(max_length=100)),
                ('pickup_postal_code', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=255)),
            ],
        ),
    ]