FROM python:3.10-slim
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --without dev --no-root
COPY . /app
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
