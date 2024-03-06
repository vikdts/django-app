from django.db import models
from django.contrib.auth.models import User

TIME_CHOICE = (
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
)

class Table(models.Model):
    SEATING_CHOICES = [
        (1,'1-2 Guests'),
        (2,'3-4 Guests'),
        (3,'5-6 Guests'),
        (4,'7-8 Guests'),
        (5,'9-10 Guests'),
        (6,'11-12 Guests'),
    ]
    seating_capcity = models.IntegerField(choices=SEATING_CHOICES)
    available = models.BooleanField(default=True)
    
    def is_available(self):
        return self.available
    
    is_available.boolean = True
    
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    email_address = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False, default='')
    date = models.DateField()
    num_guests = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=1)
    time = models.CharField(max_length=50, choices=TIME_CHOICE, blank=False, default='18:00')
    note = models.TextField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return f"Booking {self.id}, User: {self.user}"