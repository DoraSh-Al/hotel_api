from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer

# API Views
class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price_per_night', 'created_at']
    ordering = ['created_at']

class RoomDeleteView(generics.DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['room']
    ordering_fields = ['date_start']
    ordering = ['date_start']

class BookingDeleteView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# HTML Views
def rooms_list(request):
    if request.method == 'POST':
        Room.objects.create(
            description=request.POST['description'],
            price_per_night=request.POST['price_per_night']
        )
        return redirect('rooms_list')
    rooms = Room.objects.all()
    return render(request, 'rooms/rooms_list.html', {'rooms': rooms})

def bookings_list(request):
    if request.method == 'POST':
        room_id = request.POST['room_id']
        room = Room.objects.get(id=room_id)
        Booking.objects.create(
            room=room,
            date_start=request.POST['date_start'],
            date_end=request.POST['date_end']
        )
        return redirect('bookings_list')
    bookings = Booking.objects.all()
    return render(request, 'rooms/bookings_list.html', {'bookings': bookings})

def delete_room(request, pk):
    Room.objects.get(id=pk).delete()
    return redirect('rooms_list')

def delete_booking(request, pk):
    Room.objects.get(id=pk).delete()
    return redirect('bookings_list')