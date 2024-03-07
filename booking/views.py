from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking, Table


class HomeView(generic.TemplateView):
    """
    Add generic view for home page.
    """
    template_name = 'index.html'
    
class BookingsView(generic.TemplateView):
    """
    Add generic view for bookings page.
    """
    template_name = 'bookings.html'

@login_required
def create_booking(request):
    """
    This function creates and validates the booking form upon post 
    request, if successful redirects to bookings.html, else creates and
    empty form. First checks for existing bookings for the same date and guests,
    if none, returns back the form, if so refers table capacity based on the number
    of guests. Checks again based on seating capacity, saves first availble table
    and redirects to bookings.

    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            existing_bookings = Booking.objects.filter(date=booking.date, num_guests=booking.num_guests)
            if existing_bookings.exists():
                form.add_error(None, "There is no available tables for this number of guests on this date.")
                return render(request, 'book.html', {'form': form})
            if booking.num_guests <= 2:
                seating_choice = 1
            elif booking.num_guests <= 4:
                seating_choice = 2
            elif booking.num_guests <= 6:
                seating_choice = 3
            elif booking.num_guests <= 8:
                seating_choice = 4
            elif booking.num_guests <= 10:
                seating_choice = 5
            else:
                seating_choice = 6

            available_tables = Table.objects.filter(seating_capacity=seating_choice, available=True)
            if not available_tables.exists():
                form.add_error(None, "There are no available tables for this number of guests on this date.")
                return render(request, 'book.html', {'form': form})

            existing_bookings_same_time = existing_bookings.filter(time=booking.time)
            if existing_bookings_same_time.exists():
                form.add_error(None, "There are no more available tables for this number of guests on this date.")
                return render(request, 'book.html', {'form': form})

            booking.table = available_tables.first()
            booking.save()
            booking.table.available = False
            booking.table.save()
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})


@login_required
def read_booking(request):
    """
    This function renders user bookings.

    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})