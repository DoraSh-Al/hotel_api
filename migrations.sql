CREATE TABLE rooms_room (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rooms_booking (
    id SERIAL PRIMARY KEY,
    room_id INTEGER NOT NULL REFERENCES rooms_room(id) ON DELETE CASCADE,
    date_start DATE NOT NULL,
    date_end DATE NOT NULL
);

CREATE INDEX rooms_room_price_idx ON rooms_room(price_per_night);
CREATE INDEX rooms_room_created_at_idx ON rooms_room(created_at);
CREATE INDEX rooms_booking_date_start_idx ON rooms_booking(date_start);