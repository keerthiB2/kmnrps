# Generated by Django 3.1 on 2020-08-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservationinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('numberOf', models.CharField(max_length=200)),
                ('reservationdate', models.CharField(max_length=200)),
                ('reservationduration', models.CharField(max_length=200)),
                ('reservationtimezone', models.CharField(max_length=200)),
                ('tableReservation', models.CharField(max_length=200)),
                ('reservationType', models.CharField(max_length=200)),
                ('ifOther', models.CharField(max_length=200)),
            ],
        ),
    ]