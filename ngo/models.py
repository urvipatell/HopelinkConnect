import datetime
from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.utils import timezone
# Create your models here.
# Return the username attribute for displaying the object.

class signup(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    email = models.EmailField()
    phonenumber = models.CharField(max_length=13, help_text="Format: +919876543210")
    image = models.ImageField(upload_to='user_images/')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    forwhom = models.CharField(max_length=1, choices=[('u', 'User'), ('s', 'Staff')])

    def __str__(self):
        return self.username
    


class intantship(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()
    current_role = models.CharField(max_length=20, choices=[('student', 'Student'), ('job', 'Full Time Job'), ('learner', 'Full Time Learner'), ('preferNo', 'Prefer not to say'), ('other', 'Other')])
    internship_experience = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('No', 'No')])
    why_choose_ngo = models.CharField(max_length=50, choices=[('Flexible Working Hours', 'Flexible Working Hours'), ('Certificates and Letter of Recommendation', 'Certificates and Letter of Recommendation'), ('Stipends', 'Stipends'), ('Social activities', 'Social activities')])
    areas_of_interest = models.CharField(max_length=50)
    additional_skills = models.TextField()
    GENDER_CHOICES =(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),)
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    

    
    def __str__(self): 
        return self.full_name

class MoneyDonation(models.Model):
    # Name
    formType = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Phone Number
    ph_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)
    # Email
    email = models.EmailField()
    # Address
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    area_code = models.CharField(max_length=10)
    donation_amount = models.IntegerField()
    razorpay_order_id = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    country= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class SocialEvent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    type_of_event = models.CharField(max_length=255)  # Assuming this field can contain a description of the event
    activity_time = models.CharField(max_length=20)
    activity_date = models.DateField()
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    file_upload = models.FileField(upload_to='socialevent/')  # Assuming you want to upload files
    description = models.TextField()
    status = models.CharField(
        max_length=255,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending",
        )
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class UserStory(models.Model):
    name = models.CharField(max_length=255)
    story_name = models.CharField(max_length=255)
    user_story = models.TextField()
    notes = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=255,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending",
        )

    def __str__(self):
        return self.name
    
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
class HealthCamp(models.Model):
    nameofdoctor = models.CharField(max_length=255)
    nameoforg = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phonenumberarea = models.CharField(max_length=10, blank=True, null=True)
    phonenumber = models.CharField(max_length=10, blank=True, null=True)
    types1 = models.CharField(max_length=255, blank=True, null=True)
    types2 = models.CharField(max_length=255, blank=True, null=True)
    types3 = models.CharField(max_length=255, blank=True, null=True)
    types4 = models.CharField(max_length=255, blank=True, null=True)
    types5 = models.CharField(max_length=255, blank=True, null=True)
    timeinput = models.CharField(max_length=8, blank=True, null=True)
    ampm = models.CharField(max_length=2, blank=True, null=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    addrline1 = models.CharField(max_length=255)
    addresscity = models.CharField(max_length=255)
    addressstate = models.CharField(max_length=255)
    addresspostal = models.CharField(max_length=10)
    description = models.TextField()
    status = models.CharField(
        max_length=255,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending",
        )

    def __str__(self):
        return self.nameofdoctor
    
class ScholarshipApplication(models.Model):
    firstname = models.CharField(max_length=255)
    nameoforg = models.CharField(max_length=255, blank=True, null=True)
    nameofscholarship = models.CharField(max_length=255)
    email = models.EmailField()
    area = models.CharField(max_length=10, blank=True, null=True)
    phonenumber = models.CharField(max_length=10, blank=True, null=True)
    typeofscholarship = models.CharField(max_length=255)
    date = models.CharField(max_length=2)
    addrline1 = models.CharField(max_length=255)
    addresscity = models.CharField(max_length=255)
    addresstate = models.CharField(max_length=255)
    addresspostal = models.CharField(max_length=10)
    benefit = models.TextField()
    status = models.CharField(
        max_length=255,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending",
        )

    def __str__(self):
        return self.firstname


class EducationDonation(models.Model):
    # Name
    formType = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Phone Number
    ph_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)
    # Email
    email = models.EmailField()
    # Address
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    area_code = models.CharField(max_length=10)
    status = models.CharField(
        max_length=255,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending",
        )
    # Type of Donation

    type_of_donation = models.CharField(max_length=255, choices=[
        ("Financial Donations", "Financial Donations"),
        ("Clothing", "Clothing"),
        ("Shoes and Bags", "Shoes and Bags"),
        ("Kitchenware", "Kitchenware"),
        ("Books", "Books"),
        ("Toys and Games", "Toys and Games"),
        ("Arts", "Arts"),
        ("Linens", "Linens"),
        ("Hygiene Essentials", "Hygiene Essentials"),
        ("Sporting Goods", "Sporting Goods"),
        ("Furniture", "Furniture"),
        ("Other", "Other"),
        
    ])
    
    # What would you like to donate?
    what_would_you_like_to_donate = models.TextField()
    
    # Notes
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class clothDonation(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=20)
    condition = models.CharField(max_length=100)
    type_of_dress = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    note = models.TextField(blank=True)
    image = models.ImageField(upload_to='clothdonation_photos/')
    status = models.CharField(
            max_length=255,
            choices=[
                ("Pending", "Pending"),
                ("Approved", "Approved"),
                ("Rejected", "Rejected"),
            ],
            default="Pending",
            )
    
    def __str__(self):
        return self.name
    

class FoodDonation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=20)
    organization_name = models.CharField(max_length=255)
    organization_mission = models.TextField()
    date_needed = models.DateField()
    time_needed = models.CharField(max_length=255)
    pickup_address = models.CharField(max_length=255)
    pickup_city = models.CharField(max_length=100)
    pickup_state = models.CharField(max_length=100)
    pickup_postal_code = models.CharField(max_length=20)
    status = models.CharField(
        max_length=255,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending",
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.user



class Calendar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class CalendarEvent(models.Model):  # Renamed to CalendarEvent
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title






class EventImage(models.Model):
    event_choices = (
        ('Social Activity', 'Social Activity'),
        ('Impact Story', 'Impact Story'),
        ('Health Camp', 'Health Camp'),
        ('Scholarship', 'Scholarship'),
    )

    event = models.CharField(max_length=20, choices=event_choices)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.event
    

   

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback_type = models.CharField(
        max_length=20,
        choices=[('compliment', 'Compliment'), ('suggestion', 'Suggestion'), ('thought', 'thought')],
    )
    comments = models.TextField()

    def __str__(self):
        return self.email
    

class NewMember(models.Model):
    name = models.CharField(max_length=100)
    member_type = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    arriving_datetime = models.DateTimeField()
    description = models.CharField(max_length=50)
    uploaded_file = models.ImageField(upload_to='new_members/')
    status = models.CharField(
        max_length=255,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending",
        )
    def __str__(self):
        return self.member_type

class StaffNotification(models.Model):
    name = models.CharField(max_length=100)
    event_datetime = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name
