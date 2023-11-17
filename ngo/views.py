
from functools import cache
from django.shortcuts import render, redirect
from ngo.models import *
from .models import *
from .models import Notification
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
    total_users = signup.objects.filter(forwhom='u').count()
    total_staff = signup.objects.filter(forwhom='s').count()

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

    return render(request, 'ngo/admin_NewMember.html')

def calendar(request):
    return render(request, 'ngo/calendar.html')
def admin_notification (request):
    return render(request, 'ngo/admin_notifications.html')


def admin_tables(request):
    return render(request, 'ngo/admin_tables.html')

def admin_signup(request):
    return render(request, 'ngo/admin_sign-up.html')

def admin_clothdonation(request):
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
            # You need to have an 'EducationDonation' model defined.
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
    user_stories = UserStory.objects.all()
    context = {
        'user_stories': user_stories,
    }
    return render(request, 'ngo/admin_impactstory.html',context)

def admin_helthcare(request):
    health_camps = HealthCamp.objects.all()
    context = {
         'health_camps':health_camps,
    }
    return render(request, 'ngo/admin_helthcare.html',context)

def admin_scholarship(request):
    scholarship_applications = ScholarshipApplication.objects.all()
    context = {
        'scholarship_applications':scholarship_applications,
    }
    return render(request, 'ngo/admin_scholarship.html',context)

def admin_socialactivity(request):
    social_events = SocialEvent.objects.all()
    context = {
        'social_events':social_events,
    }
    return render(request, 'ngo/admin_socialactivity.html',context)

def all_donation(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'education':
            # You need to have an 'EducationDonation' model defined.
            donation = get_object_or_404(EducationDonation, id=form_id)
        elif form_type == 'food':
            # You need to have a 'FoodDonation' model defined.
            donation = get_object_or_404(FoodDonation, id=form_id)
        elif form_type == 'cloth':
            # You need to have a 'ClothDonation' model defined.
            donation = get_object_or_404(clothDonation, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        donation.status = status
        donation.save()
    
    # Query the EducationDonation model for education donations
    education_donations = EducationDonation.objects.all().order_by('-id')
    # Query the FoodDonation model for food donations in descending order
    food_donation = FoodDonation.objects.all().order_by('-id')
    # Query the ClothDonation model for cloth donations in descending order
    cloth_donation = clothDonation.objects.all().order_by('-id')
    money_donation = MoneyDonation.objects.all().order_by('-id')
    context = {
        'education_donations': education_donations,
        'food_donation': food_donation,
        'cloth_donation': cloth_donation,
        'money_donation':money_donation,
    }
    return render(request, 'ngo/all_donation.html', context)



def all_events(request):
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

    return render(request, 'ngo/all_events.html', context)


def applications(request):
    # Query the 'intantship' model to get all internship applications
    internship_applications = intantship.objects.all()

    context = {
        'internship_applications': internship_applications,
    }

    return render(request, 'ngo/applications.html', context)


from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def approve_donation(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        form_id = request.POST.get('form_id')
        status = request.POST.get('status')  # 'approve' or 'reject'

        if form_type == 'education':
            # You need to have an 'EducationDonation' model defined.
            donation = get_object_or_404(EducationDonation, id=form_id)
        elif form_type == 'food':
            # You need to have a 'FoodDonation' model defined.
            donation = get_object_or_404(FoodDonation, id=form_id)
        elif form_type == 'cloth':
            # You need to have a 'ClothDonation' model defined.
            donation = get_object_or_404(clothDonation, id=form_id)
        else:
            return JsonResponse({'success': False})

        # Update the status of the donation.
        donation.status = status
        donation.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})





def admin_notifications(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        user = request.user
        if message:
            notification = Notification(message=message,user=user)
            notification.save()
            return redirect('admin_notifications')  # Redirect to the admin notifications page or another appropriate page

    return render(request, 'ngo/admin_notifications.html')

