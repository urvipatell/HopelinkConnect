# Generated by Django 4.2.1 on 2023-12-07 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0016_rename_countrycode_signup_phonecode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarevent',
            name='calendar',
        ),
        migrations.DeleteModel(
            name='clothDonation',
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
        migrations.DeleteModel(
            name='EducationDonation',
        ),
        migrations.DeleteModel(
            name='EventImage',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='FoodDonation',
        ),
        migrations.DeleteModel(
            name='HealthCamp',
        ),
        migrations.DeleteModel(
            name='intantship',
        ),
        migrations.DeleteModel(
            name='MoneyDonation',
        ),
        migrations.DeleteModel(
            name='NewMember',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.DeleteModel(
            name='ScholarshipApplication',
        ),
        migrations.DeleteModel(
            name='signup',
        ),
        migrations.DeleteModel(
            name='SocialEvent',
        ),
        migrations.DeleteModel(
            name='StaffNotification',
        ),
        migrations.DeleteModel(
            name='UserStory',
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
        migrations.DeleteModel(
            name='CalendarEvent',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
