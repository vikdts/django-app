from django import forms
from .models import Booking
from django.forms.widgets import DateInput

class CalendarInput(DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    """
    This is the booking form used for creating and updating
    a booking, with a clendar widget for the date field and
    the specified input fields for the user.

    """
    date = forms.DateField(widget=CalendarInput)
    
    class Meta:
        model = Booking
        fields = ['name', 'email_address', 'phone', 'date', 'num_guests', 'time', 'note']