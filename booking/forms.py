from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email_address', 'phone', 'date', 'num_guests', 'time', 'note']