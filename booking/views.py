from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


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
    empty form.

    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})