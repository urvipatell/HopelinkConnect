# Generated by Django 4.2.1 on 2023-11-18 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0012_delete_newmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('member_type', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('arriving_datetime', models.DateTimeField()),
                ('description', models.CharField(max_length=50)),
                ('uploaded_file', models.ImageField(upload_to='new_members/')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=255)),
            ],
        ),
    ]
