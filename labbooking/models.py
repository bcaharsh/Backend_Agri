from django.db import models

class Booking(models.Model):
    Name=models.CharField(max_length=100)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=20)
    DateOfBooking = models.DateField()
    TimeSlot = models.TimeField()
    
    def __str__(self):
        return self.Name + " - " + str(self.DateOfBooking) + ", " + str(self.TimeSlot)  
