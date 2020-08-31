"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('hello/', views.real_view),
    path('home/',views.home_page),
    path('about/',views.about_page),
    path('contact/',views.contact_page),
    path('aboutres/',views.about_res),
    path('aboutteam/',views.about_team),
    path('standupcomedy/',views.standup_comedy),
    path('liveconcert/',views.live_concert),
    path('partynight/',views.party_night),
    path('menu/',views.hotel_menu),
    path('orderonline/',views.order_online),
    path('reservation/',views.reservation_online),
    path('gallery/',views.gallery_pics),
    path('specialevent/',views.special_events),
    path('contact_form_submission/',views.contact_form_submission),
    path('reservation_form_submission/',views.reservation_form_submission),
]
