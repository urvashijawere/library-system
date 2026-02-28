FROM python:3.12-slim

LABEL name="library_core"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

# Start Django directly
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
