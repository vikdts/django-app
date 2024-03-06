from django.contrib import admin
from booking.models import Booking, Table

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ('name', 'email_address', 'phone', 'date', 'num_guests', 'time', 'note')