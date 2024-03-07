from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required


class HomeView(generic.TemplateView):
    """
    Add generic view for home page.
    """
    template_name = 'index.html'

