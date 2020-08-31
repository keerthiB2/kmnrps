from django.contrib import admin

# Register your models here.
from .models import contactinfo
from .models import reservationinfo
admin.site.register(contactinfo)
admin.site.register(reservationinfo)
