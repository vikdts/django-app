from django import forms
from .models import Booking
from django.forms.widgets import DateInput

class CalendarInput(DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email_address', 'phone', 'date', 'num_guests', 'time', 'note']