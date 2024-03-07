from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


class HomeView(generic.TemplateView):
    """
    Add generic view for home page.
    """
    template_name = 'index.html'

