from django.db import models

# Create your models here.
class contactinfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.name
class reservationinfo(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    numberOf=models.CharField(max_length=200)
    reservationdate=models.CharField(max_length=200)
    reservationduration=models.CharField(max_length=200)
    reservationtimezone=models.CharField(max_length=200)
    tableReservation=models.CharField(max_length=200)
    reservationType=models.CharField(max_length=200)
    ifOther=models.CharField(max_length=200)

    def __str__(self):
        return self.firstname
