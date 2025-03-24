from django.urls import path
from rooms.views import (
    RoomListCreateView, RoomDeleteView, BookingListCreateView, BookingDeleteView,
    rooms_list, bookings_list, delete_room, delete_booking
)

urlpatterns = [
    # API
    path('rooms/', RoomListCreateView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDeleteView.as_view(), name='room-delete'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDeleteView.as_view(), name='booking-delete'),
    # HTML
    path('', rooms_list, name='rooms_list'),
    path('rooms/add/', rooms_list, name='rooms_add'),
    path('rooms/delete/<int:pk>/', delete_room, name='delete_room'),
    path('bookings/', bookings_list, name='bookings_list'),
    path('bookings/add/', bookings_list, name='bookings_add'),
    path('bookings/delete/<int:pk>/', delete_booking, name='delete_booking'),
]