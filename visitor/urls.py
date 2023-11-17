from django.urls import path

from. import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('event', views.event, name="event"),
    path('contact', views.contact, name="contact"),
    path('gallery', views.gallery, name="gallery"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('notification', views.notification, name="notification"),
    path('registration', views.registration, name="registration"),
    path('intant', views.intant, name="intant"),
    path('userabout', views.user_about, name="userabout"),
    path('userevent', views.user_event, name="userevent"),
    path('usercontact', views.user_contact, name="usercontact"),
    path('map', views.map, name="map"),
    path('usergallery', views.user_gallery, name="usergallery"),
    path('userhome', views.user_index, name="userhome"),
    path('userprofile', views.user_profile, name="userprofile"),
    path('userdonation', views.user_donation, name="userdonation"),
    path('userdeshbord', views.user_deshbord, name="userdeshbord"),
    path('userfeedback', views.user_feedback, name="userfeedback"),
    path('newmember', views.new_member, name="newmember"),
    path('user_notification/', views.user_notification, name='user_notification'),
    path('fetch_notifications/', views.fetch_notifications, name='fetch_notifications'),



    path('staffdeshbord', views.staff_deshbord, name="staffdeshbord"),
    path('staffdonationre', views.staff_donation, name="staffdonationre"),
    path('staffindex', views.staff_index, name="staffindex"),
    path('staffinvoice', views.staff_invoice, name="staffinvoice"),
    path('staffmap', views.staff_map, name="staffmap"),
    path('staffmediagallery', views.staff_media, name="staffmediagallery"),
    path('staff_money_do', views.staff_money_do, name="staff_money_do"),
    path('staffnotification', views.staff_notification, name="staffnotification"),
    path('staffprofile', views.staff_profile, name="staffprofile"),
    path('staffproject', views.staff_project, name="staffproject"),
    path('staffevent', views.staffevent, name="staffevent"),
   
    
    
]   