
from collections import UserDict
from multiprocessing import connection
from pyexpat.errors import messages
from django.shortcuts import *
from django.contrib.auth.models import User
from ngo.models import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import razorpay
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Count
from django.http import JsonResponse

# Create your views here.

def index(request):
    notifications = StaffNotification.objects.all()
    return render(request, 'visitor/index.html',{'notifications': notifications})

def about (request):
    return render(request, 'visitor/about.html')

def contact (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)

        # Create a new InternshipApplication object and save it to the database
        contact = ContactUs(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        subject = subject
        message = message
        from_email = 'hopelinkconnect@gmail.com'
        recipient_list = [email] 

        send_mail(subject, message, from_email, recipient_list)
        contact.save()
    return render(request, 'visitor/contact.html')

def event (request):
    return render(request, 'visitor/event.html')

def gallery (request):
    health_camp_images = EventImage.objects.filter(event='Health Camp')
    social_activity_images = EventImage.objects.filter(event='Social Activity')
    impact_story_images = EventImage.objects.filter(event='Impact Story')
    scholarship_images = EventImage.objects.filter(event='Scholarship')

    context = {
        'health_camp_images': health_camp_images,
        'social_activity_images': social_activity_images,
        'impact_story_images': impact_story_images,
        'scholarship_images': scholarship_images,
    }
    # images = EventImage.objects.all()
    # print(images)
    # if images:
    return render(request, 'visitor/gallery.html', context)
    # else:
    #     messages.error(request, 'Profile data not found')
    #     return redirect('home')


def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                messages.warning(request, "Welcome Admin...")
                return redirect("admindashboard")
        else:
            try:
                user_profile = signup.objects.get(username=username,password=password)
                request.session['username'] = user_profile.username
                request.session['profileImage'] = user_profile.image.url
                if user_profile.forwhom == 'u':
                    return redirect('userdeshbord')
                elif user_profile.forwhom == 's':
                    return redirect('staffdeshbord')
                
            except signup.DoesNotExist:
                # Handle the case where the user profile does not exist
                pass

        # If authentication fails, display an error message
        messages.error(request, "Invalid login credentials. Please try again.")
    return render(request, 'visitor/login.html')



def registration(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')
        forwhom = request.POST.get('forwhom')

        # Check if a user with the same username already exists
        if signup.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('registration')

        # Create a user profile associated with the user
        profile = signup.objects.create(
            username=username,
            email=email,
            password=password,
            name=name,
            phonenumber=phonenumber,
            gender=gender,
            image=image,
            forwhom=forwhom
        )
        user_profile = signup.objects.get(username=username)
        request.session['username'] = user_profile.username
        request.session['profileImage'] = user_profile.image.url
        
        if forwhom == 'u':
            # Redirect to the user dashboard
            return redirect('userdeshbord')
        elif forwhom == 's':
            # Redirect to the staff dashboard
            return redirect('staffdeshbord')

    return render(request, 'visitor/registration.html')

def user_profile(request):
    username = request.session.get('username')
    if username:
        profile = signup.objects.filter(username=username).first()
        if profile:
            return render(request, 'user/user_profile.html', {'profile': profile})
        else:
            messages.error(request, 'Profile data not found')
            return redirect('home')
    else:
        messages.error(request, 'Please login first')
        return redirect('login')
    
def intant (request):
    if request.method == 'POST':
        # Get data from the form
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phonenumber')
        age = request.POST.get('age')
        current_role = request.POST.get('role')
        internship_experience = request.POST.get('user-recommend')
        gender = request.POST.get('gender')
        why_choose_ngo = request.POST.get('mostLike')
        areas_of_interest = ','.join(request.POST.getlist('prefer'))
        additional_skills = request.POST.get('comment')

        # Create a new InternshipApplication object and save it to the database
        application = intantship(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            age=age,    
            current_role=current_role,
            internship_experience=internship_experience,
            gender=gender,
            why_choose_ngo=why_choose_ngo,
            areas_of_interest=areas_of_interest,
            additional_skills=additional_skills,
        )
        
        application.save()
    
    return render(request, 'visitor/intant.html')

def user_index (request):
    # profileImage = request.session.get('image')
    notifications = StaffNotification.objects.all()
    return render(request, 'user/user_index.html',{'notifications': notifications})

def user_about (request):
    return render(request, 'user/user_about.html')

def user_contact (request):
    return render(request, 'user/user_contact.html')

def user_feedback(request):
    if request.method == 'POST':
        # Handle the form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_type = request.POST.get('feedbackType')
        comments = request.POST.get('comments')

        feedback = Feedback(name=name, email=email, feedback_type=feedback_type, comments=comments)
        feedback.save()

    return render(request, 'user/user_feedback.html')

def map (request):
    return render(request, 'user/map.html')

def user_gallery (request):
    return render(request, 'user/user_gallery.html')

# def getSessionData(request):
#     username = request.session.get('username')
#     profileImage = request.session.get('profileImage')
#     userDetails = {
#         'username': username,
#         'profileImage': profileImage
#     }
#     return userDetails
@login_required
def user_deshbord (request):
    return render(request, 'user/user_deshbord.html')



def logout(request):
    # logout(request)
    del request.session['username']
    del request.session['profileImage']
    messages.success(request,"Suceessfull logged in")
    return render(request, 'visitor/index.html')    
    # return redirect('home')

@csrf_exempt
def user_donation(request):
    print("Hello", request)
    if request.method == 'POST':
        # Extract data from the form
        print(request.POST.get('formType'))
        if request.POST.get('formType') == 'education':
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            ph_code = request.POST.get('phonecode')
            phone_number = request.POST.get('phonenumber')
            email = request.POST.get('email')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postal_code = request.POST.get('portno')
            type_of_donation = request.POST.get('type_of_donation')  # Corrected field name
            what_to_donate = request.POST.get('whatWould')
            notes = request.POST.get('notes')

            # Create a new Donation object and save it to the database
            education = EducationDonation(
                first_name=first_name,
                last_name=last_name,
                ph_code=ph_code,
                phone_number=phone_number,
                email=email,
                address=address,
                city=city,
                state=state,
                area_code=postal_code,
                type_of_donation = type_of_donation,
                what_would_you_like_to_donate = what_to_donate,
                notes=notes
            )
            education.save()

        elif request.POST.get('formType') == "cloth" :
            print(request.POST)
            first_name = request.POST['first']
            last_name = request.POST['last']
            email = request.POST['email']
            phone_code = request.POST['phonecode']
            phone_number = request.POST['phonenumber']
            condition = request.POST['condition']
            type_of_dress = request.POST['type_of_dress']
            size = request.POST['size']
            note = request.POST['note']
            image = request.FILES.get('image')

            # Create a new Donation object and save it to the database
            cloth = clothDonation(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_code=phone_code,
            phone_number=phone_number,
            condition=condition,
            type_of_dress=type_of_dress,
            size=size,
            note=note,
            image=image 
            )
            cloth.save()

        elif request.POST.get('formType') == "food" :   
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            phonecode = request.POST['phonecode']
            phonenumber = request.POST['phonenumber']
            organization = request.POST['organization']
            organizationmission = request.POST['organizationmission']
            date = request.POST['date']
            hour = request.POST['hour']
            ampm = request.POST['ampm']
            pickup_address = request.POST['pickup_address']
            pickup_city = request.POST['pickup_city']
            pickup_state = request.POST['pickup_state']
            pickup_postal = request.POST['pickup_postal']

        # Create a new Donation object and save it to the database
            Food= FoodDonation(
            first_name=firstname,
            last_name=lastname,
            email=email,
            phone_code=phonecode,
            phone_number=phonenumber,
            organization_name=organization,
            organization_mission=organizationmission,
            date_needed=date,
            time_needed=f"{hour} {ampm}",
            pickup_address=pickup_address,
            pickup_city=pickup_city,
            pickup_state=pickup_state,
            pickup_postal_code=pickup_postal
            )
            Food.save()
       
        elif request.POST.get('formType') == "money" : 
            print(request.POST.get('formType'))  
            client = razorpay.Client(
            auth=("rzp_test_izLKitcUJEXjP9", "o7qk1ktJiwT6BpOv6U6UmYdX"))
            amount = int(request.POST.get('donation_amount'))* 100
            payment = client.order.create({'amount': amount, 'currency': 'INR',
                                        'payment_capture': '1'})
            razorpay_order_id = payment['id']
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            ph_code = request.POST.get('phonecode')
            phone_number = request.POST.get('phonenumber')
            email = request.POST.get('email')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postal_code = request.POST.get('portno')
            country=request.POST.get('country')
            donation_amount = request.POST.get('donation_amount')  # Corrected field name]
            
            # Create a new Donation object and save it to the database
            money = MoneyDonation(
                first_name=first_name,
                last_name=last_name,
                ph_code=ph_code,
                phone_number=phone_number,
                email=email,
                address=address,
                city=city,
                state=state,
                area_code=postal_code,
                country=country,
                donation_amount = donation_amount,
                currency='INR',
                razorpay_order_id=razorpay_order_id
            )
            money.save()            
    return render(request, 'user/user_donation.html')

def user_event (request):
    print(request.method)
    if request.method == 'POST':
        # Extract data from the form
        if request.POST.get('formType') == 'social':
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email = request.POST.get('email')
            phone_area = request.POST.get('phonenumberarea')
            phone_number = request.POST.get('phonenumber')
            type1 = request.POST.get('type1')
            type2 = request.POST.get('type2')
            type3 = request.POST.get('type3')
            type4 = request.POST.get('type4')
            type5 = request.POST.get('type5')
            time_input = request.POST.get('timeinput')
            ampm = request.POST.get('ampm')
            date = request.POST.get('date')
            address_line1 = request.POST.get('addrline1')
            address_city = request.POST.get('addresscity')
            address_state = request.POST.get('addressstate')
            address_postal = request.POST.get('addresspostal')
            file_upload = request.FILES.get('fileupload')  # Handle file upload
            description = request.POST.get('description')

            # Create a new SocialEvent instance and save it to the database
            social_event = SocialEvent(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=f"{phone_area} {phone_number}",
            type_of_event=f"{type1}, {type2}, {type3}, {type4}, {type5}",
            activity_time=f"{time_input} {ampm}",
            activity_date=date,
            address_line1=address_line1,
            city=address_city,
            state=address_state,
            postal_code=address_postal,
            file_upload=file_upload,
            description=description,
            )
            social_event.save()

        elif request.POST.get('formType') == "impact" :
            name = request.POST.get('storyid')
            story_name = request.POST.get('storyname')
            user_story = request.POST.get('userstory')
            notes = request.POST.get('notes')
            
            # Create a UserStory instance and save it to the database
            user_story_instance = UserStory(
                name=name,
                story_name=story_name,
                user_story=user_story,
                notes=notes
            )
            user_story_instance.save()
        
        elif request.POST.get('formType') == "healthcamp" :
            nameofdoctor = request.POST.get('nameofdoctor')
            nameoforg = request.POST.get('nameoforg')
            email = request.POST.get('email')
            phonenumberarea = request.POST.get('phonenumberarea')
            phonenumber = request.POST.get('phonenumber')
            types1 = request.POST.get('types1')
            types2 = request.POST.get('types2')
            types3 = request.POST.get('types3')
            types4 = request.POST.get('types4')
            types5 = request.POST.get('types5')
            timeinput = request.POST.get('timeinput')
            ampm = request.POST.get('ampm', 'AM')
            date = request.POST.get('date')
            addrline1 = request.POST.get('addrline1')
            addresscity = request.POST.get('addresscity')
            addressstate = request.POST.get('addressstate')
            addresspostal = request.POST.get('addresspostal')
            description = request.POST.get('description')

            # Create a HealthCamp instance and save it to the database
            healthcamp= HealthCamp(
                nameofdoctor=nameofdoctor,
                nameoforg=nameoforg,
                email=email,
                phonenumberarea=phonenumberarea,
                phonenumber=phonenumber,
                types1=types1,
                types2=types2,
                types3=types3,
                types4=types4,
                types5=types5,
                timeinput=timeinput,
                ampm=ampm,
                date=date,
                addrline1=addrline1,
                addresscity=addresscity,
                addressstate=addressstate,
                addresspostal=addresspostal,
                description=description
            )
            healthcamp.save()

        elif request.POST.get('formType') == "scholarship" :
            firstname = request.POST.get('firstname')
            nameoforg = request.POST.get('nameoforg', '')
            nameofscholarship = request.POST.get('nameofscholarship')
            email = request.POST.get('email')
            area = request.POST.get('area', '')
            phonenumber = request.POST.get('phonenumber', '')
            typeofscholarship = request.POST.get('typeofscholarship')
            date = request.POST.get('date')
            addrline1 = request.POST.get('addrline1')
            addresscity = request.POST.get('addresscity')
            addresstate = request.POST.get('addresstate')
            addresspostal = request.POST.get('addresspostal')
            benefit = request.POST.get('benefit')

            # Create a new ScholarshipApplication object and save it
            application = ScholarshipApplication(
                firstname=firstname,
                nameoforg=nameoforg,
                nameofscholarship=nameofscholarship,
                email=email,
                area=area,
                phonenumber=phonenumber,
                typeofscholarship=typeofscholarship,
                date=date,
                addrline1=addrline1,
                addresscity=addresscity,
                addresstate=addresstate,
                addresspostal=addresspostal,
                benefit=benefit
            )
            application.save()
    return render(request, 'user/user_event.html')



@login_required
def staff_deshbord (request):
     # Calculate the total donations for each type
    education_total = EducationDonation.objects.count()
    cloth_total = clothDonation.objects.count()
    food_total = FoodDonation.objects.count()
    money_total = MoneyDonation.objects.count()
    totalMember = NewMember.objects.count()
    oldMember = NewMember.objects.filter(member_type = "Old").count()
    newMember = NewMember.objects.filter(member_type = "Child").count()

    print(f"Education Total: {education_total}")
    print(f"Cloth Total: {cloth_total}")
    print(f"Food Total: {food_total}")
    print(f"Money Total: {money_total}")
    print(f"Old: {oldMember}")

    # Calculate the grand total of all donations
    grand_total = education_total + cloth_total + food_total + money_total
    print(f"Grand Total: {grand_total}")

    context = {
        'education_total': education_total,
        'cloth_total': cloth_total,
        'food_total': food_total,
        'money_total': money_total,
        'grand_total': grand_total,
        'totalMember': totalMember,
        'oldMember': oldMember,
        'newMember': newMember
    }


    return render(request, 'staff/staff_deshbord.html', context)

def staff_profile (request):
  username = request.session.get('username')
  if username:
        profile = signup.objects.filter(username=username).first()
        if profile:
            return render(request, 'staff/staff_profile.html', {'profile': profile})
        else:
            messages.error(request, 'Profile data not found')
            return redirect('home')
  else:
        messages.error(request, 'Please login first')
        return redirect('login')
    

def staff_donation (request):

    return render(request, 'staff/staff_donation_re.html')

def staff_index (request):

    return render(request, 'staff/staff_index.html')

def staff_invoice (request):

    return render(request, 'staff/staff_invoice.html')

def staff_map (request):

    return render(request, 'staff/staff_map.html')

def staff_media (request):
    if request.method == 'POST':
        event = request.POST['event']
        description = request.POST['description']
        image = request.FILES['file']
        # Create a new InternshipApplication object and save it to the database
        eventimage = EventImage (
            event=event,
            description=description,
            image=image
        )
        
        eventimage.save()

    health_camp_images = EventImage.objects.filter(event='Health Camp')
    social_activity_images = EventImage.objects.filter(event='Social Activity')
    impact_story_images = EventImage.objects.filter(event='Impact Story')
    scholarship_images = EventImage.objects.filter(event='Scholarship')

    context = {
        'health_camp_images': health_camp_images,
        'social_activity_images': social_activity_images,
        'impact_story_images': impact_story_images,
        'scholarship_images': scholarship_images,
    }
    return render(request, 'staff/staff_media_gallery.html', context)


def staffevent(request):
    # Query the database for all events of different types
    social_events = SocialEvent.objects.all()
    user_stories = UserStory.objects.all()
    health_camps = HealthCamp.objects.all()
    scholarship_applications = ScholarshipApplication.objects.all()

    context = {
        'social_events': social_events,
        'user_stories': user_stories,
        'health_camps': health_camps,
        'scholarship_applications': scholarship_applications,
    }

    return render(request, 'staff/staff_event.html', context)

def staff_notification (request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        event_datetime = request.POST.get('datetime')
        description = request.POST.get('description')

        # Create a new StaffNotification instance and save it to the database
        staff_notification = StaffNotification(
            name=name,
            event_datetime=event_datetime,
            description=description,
        )
        staff_notification.save()
    
    notifications = StaffNotification.objects.all()
    return render(request, 'staff/staff_notification.html', {'notifications': notifications})



def notification(request):
    notifications = StaffNotification.objects.all()
    return render(request, 'staff/staff_notification.html', {'notifications': notifications})



def staff_project (request):

    return render(request, 'staff/staff_project.html')


def staff_money_do(request):
    # Query the EducationDonation model for education donations
    education_donations = EducationDonation.objects.filter(status='Approved').order_by('-id')

    # Query the FoodDonation model for food first_name in descending order
    food_donation = FoodDonation.objects.filter(status='Approved').order_by('-id')

    # Query the ClothDonation model for cloth donations in descending order
    cloth_donation = clothDonation.objects.filter(status='Approved').order_by('-id')
   
    context = {
        'education_donations': education_donations,
        'food_donation': food_donation,
        'cloth_donation': cloth_donation,
    }

    return render(request, 'staff/staff_money_do.html', context)

def user_notification(request):
    # Get notifications for the currently logged-in user
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-timestamp')

    # Mark notifications as read
    for notification in notifications:
        notification.is_read = True
        notification.save()

    return render(request, 'user/user_notification.html', {'notifications': notifications})



def fetch_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-timestamp')
    notification_data = [{'message': notification.message, 'timestamp': notification.timestamp.strftime('%Y-%m-%d %H:%M')} for notification in notifications]
    return JsonResponse({'notifications': notification_data})



def donation_totals(request):
    # Calculate the total donations for each type
    education_total = EducationDonation.objects.count()
    cloth_total = clothDonation.objects.count()
    food_total = FoodDonation.objects.count()
    money_total = MoneyDonation.objects.count()

    print(f"Education Total: {education_total}")
    print(f"Cloth Total: {cloth_total}")
    print(f"Food Total: {food_total}")
    print(f"Money Total: {money_total}")

    # Calculate the grand total of all donations
    grand_total = education_total + cloth_total + food_total + money_total
    print(f"Grand Total: {grand_total}")

    context = {
        'education_total': education_total,
        'cloth_total': cloth_total,
        'food_total': food_total,
        'money_total': money_total,
        'grand_total': grand_total,
    }

   

    return render(request, 'staff/staff_deshbord.html',context) 

def new_member(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        member_type = request.POST.get('dropdown')
        age = request.POST.get('age')
        arriving_datetime = request.POST.get('datetime')
        description = request.POST.get('description')  # Use '' as a default value
        uploaded_file = request.FILES['file']

        # Create a new member instance and save it to the database
        new_member = NewMember(
        name=name,
        member_type=member_type,
        age=age,
        arriving_datetime=arriving_datetime,
        description=description,
        uploaded_file = uploaded_file
        )
        new_member.save()
    return render(request, 'staff/ngo_member.html')