import pytest

from src.rooms.models import Booking, Room


@pytest.mark.django_db
def test_room_creation():
    room = Room.objects.create(description="Test Room", price_per_night=50.00)
    assert room.description == "Test Room"
    assert room.price_per_night == 50.00

@pytest.mark.django_db
def test_booking_creation():
    room = Room.objects.create(description="Test Room", price_per_night=50.00)
    booking = Booking.objects.create(
        room=room,
        date_start="2025-04-01",
        date_end="2025-04-03"
    )
    assert booking.room == room
    assert str(booking.date_start) == "2025-04-01"
