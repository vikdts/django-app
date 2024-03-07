from booking import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('bookings', views.read_booking, name='bookings'),
    path('update_booking/<int:pk>/', views.update_booking, name='update_booking'),
    path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('menu', views.MenuView.as_view(), name='menu'),
]
