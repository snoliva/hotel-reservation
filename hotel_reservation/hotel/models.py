from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
        ('Individual', 'Individual'),
        ('Doble', 'Doble')
    ]

    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)

class Reservation(models.Model):
    guest_name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()