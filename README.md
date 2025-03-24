# Hotel API
Сервис для управления номерами отеля и бронированиями.

## Требования
- Python 3.10+
- Poetry
- PostgreSQL

## Запуск
1. Клонируйте репозиторий: `git clone <url> && cd hotel_api`
2. Установите зависимости: `poetry install`
3. Установите PostgreSQL и создайте базу: `createdb -U postgres hotel_db`
4. Примените таблицы: `psql -U postgres -d hotel_db -f migrations.sql`
5. Активируйте окружение и запустите сервер: `cd src && poetry shell && python manage.py runserver`

## API
- **POST /rooms/** — Добавить номер: `{"description": "Cozy room", "price_per_night": 50.00}`
- **DELETE /rooms/<id>/** — Удалить номер
- **GET /rooms/?ordering=price_per_night** — Список номеров (сортировка: `price_per_night`, `-price_per_night`, `created_at`, `-created_at`)
- **POST /bookings/** — Добавить бронь: `{"room": 1, "date_start": "2025-04-01", "date_end": "2025-04-03"}`
- **DELETE /bookings/<id>/** — Удалить бронь
- **GET /bookings/?room=1** — Список броней номера (сортировка по `date_start`)

## Фронтенд
- **GET /** — Страница бронирования: выберите номер и даты, добавьте бронь
- **GET /bookings/** — Список броней с возможностью отмены
- Стили: размытый фон, оранжево-белая цветовая схема