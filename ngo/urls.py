
from django.urls import path
from. import views

urlpatterns = [
    path('admindashboard', views.admin_dashboard, name="admindashboard"),
    path('adminnotification', views.admin_notification, name="adminnotification"),
    path('adminNewmember', views.admin_newMember, name="adminNewmember"),
    path('admintable', views.admin_tables, name="admintable"),
    path('adminsignup', views.admin_signup, name="adminsignup"),
    path('all_donation/', views.all_donation, name='all_donation'),
    path('all_events/', views.all_events, name='all_events'),
    path('applications/', views.applications, name='applications'),
    path('calendar/', views.calendar, name='calendar'), 
    path('approve_donation/', views.approve_donation, name='approve_donation'),
    path('admin_notifications/', views.admin_notifications, name='admin_notifications'),   
    path('admin_edudonation/', views.admin_edudonation, name='admin_edudonation'),   
    path('admin_moneydonation/', views.admin_money, name='admin_moneydonation'),   
    path('admin_clothdonation/', views.admin_clothdonation, name='admin_clothdonation'),   
    path('admin_fooddonation/', views.admin_fooddonation, name='admin_fooddonation'),   
    path('admin_impactstory/', views.admin_impactstory, name='admin_impactstory'),   
    path('admin_helthcare/', views.admin_helthcare, name='admin_helthcare'),   
    path('admin_scholarship/', views.admin_scholarship, name='admin_scholarship'),   
    path('admin_socialactivity/', views.admin_socialactivity, name='admin_socialactivity'),   

   


    

    

]   