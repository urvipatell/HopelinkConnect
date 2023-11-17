from django.contrib import admin
# Register your models here.
from django.utils.html import format_html
from ngo.models import Notification
# Register your models here.
from .models import *

admin.site.register(signup)
admin.site.register(intantship)
admin.site.register(EducationDonation)
admin.site.register(clothDonation)
admin.site.register(FoodDonation)
admin.site.register(SocialEvent)
admin.site.register(UserStory)
admin.site.register(HealthCamp)
admin.site.register(ScholarshipApplication)
admin.site.register(MoneyDonation)
admin.site.register(Notification)
admin.site.register(ContactUs)
admin.site.register(EventImage)
admin.site.register(Feedback)
admin.site.register(NewMember)
admin.site.register(StaffNotification)
admin.site.register(Calendar)
admin.site.register(CalendarEvent)
