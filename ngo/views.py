
from functools import cache
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ngo.models import *
from .models import *



# Create your views here.
def admin_dashboard (request):
     # Calculate the total donations for each type
    education_total = EducationDonation.objects.count()
    cloth_total = clothDonation.objects.count()
    food_total = FoodDonation.objects.count()
    money_total = MoneyDonation.objects.count()
    totalMember = NewMember.objects.count()
    oldMember = NewMember.objects.filter(member_type = "Old").count()
    newMember = NewMember.objects.filter(member_type = "Child").count()
    total_amount = MoneyDonation.objects.aggregate(total=models.Sum('donation_amount'))

    # Calculate the grand total of all donations
    grand_total = education_total + cloth_total + food_total + money_total
    total_users = signup.objects.filter(forwhom='user').count()
    total_staff = signup.objects.filter(forwhom='staff').count()

    context = {
        'education_total': education_total,
        'cloth_total': cloth_total,
        'food_total': food_total,
        'money_total': money_total,
        'grand_total': grand_total,
        'totalMember': totalMember,
        'oldMember': oldMember,
        'newMember': newMember, 
        'total_amount' : total_amount,
        'total_users': total_users, 
         'total_staff':total_staff,
          }
    
    return render(request, 'ngo/admin_dashboard.html',context)

def admin_newMember(request): #new member 
    if request.method == 'POST':
        
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        donation = get_object_or_404(NewMember, id=form_id)
      

        # Update the status of the donation.
        donation.status = status
        donation.save()

    new_member = NewMember.objects.all()
    context = {
        'new_member': new_member
    }

    return render(request, 'ngo/admin_NewMember.html',context)


def admin_clothdonation(request):

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'cloth':
        
             donation = get_object_or_404(clothDonation, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        donation.status = status
        donation.save()
    
    cloth_donation = clothDonation.objects.all().order_by('-id')
    context = {
        'cloth_donation': cloth_donation
    }
    return render(request, 'ngo/admin_clothdonation.html', context)


def admin_edudonation(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'education':
      
            donation = get_object_or_404(EducationDonation, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        donation.status = status
        donation.save()
    education_donations = EducationDonation.objects.all().order_by('-id')
    context = {
        'education_donations': education_donations
    }
    return render(request, 'ngo/admin_edudonation.html', context)

def admin_fooddonation(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'food':
            donation = get_object_or_404(FoodDonation, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        donation.status = status
        donation.save()
    food_donation = FoodDonation.objects.all().order_by('-id')
    context = {
        'food_donation': food_donation
    }
    return render(request, 'ngo/admin_fooddonation.html', context)

def admin_money(request):
    money_donation = MoneyDonation.objects.all().order_by('-id')
    context = {
        'money_donation':money_donation,
    }
    return render(request, 'ngo/admin_moneydonation.html', context)


def admin_impactstory(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'impact':
            event = get_object_or_404(UserStory, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        event.status = status
        event.save()

    user_stories = UserStory.objects.all()
    context = {
        'user_stories': user_stories,
    }
    return render(request, 'ngo/admin_impactstory.html',context)

def admin_helthcare(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'healthcamp':
            event = get_object_or_404(HealthCamp, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        event.status = status
        event.save()

    health_camps = HealthCamp.objects.all()
    context = {
         'health_camps':health_camps,
    }
    return render(request, 'ngo/admin_helthcare.html',context)

def admin_scholarship(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'scholarship':
            event = get_object_or_404(ScholarshipApplication, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        event.status = status
        event.save()

    scholarship_applications = ScholarshipApplication.objects.all()
    context = {
        'scholarship_applications':scholarship_applications,
    }
    return render(request, 'ngo/admin_scholarship.html',context)

def admin_socialactivity(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'social':
            event = get_object_or_404(SocialEvent, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        event.status = status
        event.save()

    social_events = SocialEvent.objects.all()
    context = {
        'social_events':social_events,
    }
    return render(request, 'ngo/admin_socialactivity.html',context)

def staff(request):
    if request.method == 'POST':
        
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        staff= get_object_or_404(signup, id=form_id)
      

        # Update the status of the donation.
        staff.status = status
        staff.save()

    staff = signup.objects.filter(forwhom='staff')

    context = {
        'staff': staff
    }

    return render(request, 'ngo/Staff.html',context)



def user(request):
    
    user= signup.objects.filter(forwhom='user')

    context = {
        'user': user,
    }

    return render(request, 'ngo/user.html',context)

def applications(request):
    # Query the 'intantship' model to get all internship applications
    internship_applications = intantship.objects.all()

    context = {
        'internship_applications': internship_applications,
    }

    return render(request, 'ngo/applications.html', context)


def admin_notifications(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        user = request.user
        if message:
            notification = Notification(message=message,user=user)
            notification.save()
            return redirect('admin_notifications')  # Redirect to the admin notifications page or another appropriate page

    return render(request, 'ngo/admin_notifications.html')


def admin_staffnotification(request):
    if request.method == 'POST':
        # Handle the form submission
        username = request.POST.get('username')
        email = request.POST.get('email')
        time = request.POST.get('time')
        comments = request.POST.get('comments')

        # Assuming you are using the currently logged-in user
        user = request.user

        # Create a StaffNotification object and save it
        notification = StaffNotification(user=user, username=username, email=email, time=time, comments=comments)
        notification.save()

        return redirect('admin_staffnotification') 
    
    return render(request, 'ngo/admin_Staffnotification.html')

def calendar(request):
    return render(request, 'ngo/calendar.html')

def admin_notification (request):
    return render(request, 'ngo/admin_notifications.html')

def admin_tables(request):
    return render(request, 'ngo/admin_tables.html')

def admin_signup(request):
    return render(request, 'ngo/admin_sign-up.html')



