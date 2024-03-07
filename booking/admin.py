from django.contrib import admin
from booking.models import Booking, Table

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Defines the Booking model custom interface in admin with specified list of fields.
    
    """
    model = Booking
    list_display = ('id', 'user', 'name', 'email_address', 'phone', 'date', 'num_guests', 'time', 'note')
    
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Defines the Table model custom interface in admin with choice list of seating_capacity
    and availability.
    
    """
    list_display = ('seating_capacity', 'available')