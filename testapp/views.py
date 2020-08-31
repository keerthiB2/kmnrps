from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from .models import contactinfo
from .models import reservationinfo

def real_view(request):
    #return HttpResponse('<h1>I am a Disco Dancer</h1>')
    return render(request,'testapptemp/results.html')

def home_page(request):
    return render(request,'testapptemp/home.html')

def about_page(request):
    return render(request,'testapptemp/about.html')

def about_res(request):
    return render(request,'testapptemp/aboutres.html')

def about_team(request):
    return render(request,'testapptemp/aboutteam.html')

def standup_comedy(request):
    return render(request,'testapptemp/standupcomedy.html')

def live_concert(request):
    return render(request,'testapptemp/liveconcert.html')

def party_night(request):
    return render(request,'testapptemp/partynight.html')

def gallery_pics(request):
    return render(request,'testapptemp/gallery.html')

def reservation_online(request):
    return render(request,'testapptemp/reservation.html')

def hotel_menu(request):
    return render(request,'testapptemp/menu.html')

def order_online(request):
    return render(request,'testapptemp/orderonline.html')

def special_events(request):
    return render(request,'testapptemp/specialevent.html')

def contact_form_submission(request):
    print("Hello form is submitted")
    name=request.POST["name"]
    email=request.POST["email"]
    message=request.POST["message"]

    contact_info = contactinfo(name=name,email=email,message=message)
    contact_info.save()

    return render(request,'testapptemp/contact.html')

def reservation_form_submission(request):
    print("Form is submitted")
    firstname=request.POST["q20_fullName[first]"]
    lastname=request.POST["q20_fullName[last]"]
    email=request.POST["q21_email"]
    phone=request.POST["q6_phone"]
    numberOf=request.POST["q17_numberOf"]
    reservationdate=request.POST["q24_reservation[date]"]
    reservationduration=request.POST["q24_reservation[duration]"]
    reservationtimezone=request.POST["q24_reservation[timezone]"]
    tableReservation=request.POST["q13_tableReservation"]
    reservationType=request.POST["q16_reservationType"]
    ifOther=request.POST["q22_ifOther"]
    reservation_info = reservationinfo(firstname=firstname,lastname=lastname,email=email,phone=phone,numberOf=numberOf,reservationdate=reservationdate,reservationduration=reservationduration,reservationtimezone=reservationtimezone,
    tableReservation=tableReservation,reservationType=reservationType,ifOther=ifOther)
    reservation_info.save()
    return render(request,'testapptemp/reservation.html')


def contact_page(request):
    return render(request,'testapptemp/contact.html')
