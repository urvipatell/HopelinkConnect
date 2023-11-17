# Generated by Django 4.2.1 on 2023-11-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0047_alter_feedback_feedback_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('member_type', models.CharField(choices=[('Child', 'Child'), ('Old', 'Old')], max_length=10)),
                ('age', models.IntegerField()),
                ('arriving_datetime', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='New_members/')),
            ],
        ),
    ]