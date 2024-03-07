from booking import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('bookings', views.read_booking, name='bookings'),
]
