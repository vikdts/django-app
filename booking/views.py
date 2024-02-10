from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    """
    Add generic view for home page.
    """
    template_name = 'index.html'
