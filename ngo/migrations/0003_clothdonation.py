# Generated by Django 4.2.1 on 2023-11-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0002_delete_clothdonation'),
    ]

    operations = [
        migrations.CreateModel(
            name='clothDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
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
    ]
