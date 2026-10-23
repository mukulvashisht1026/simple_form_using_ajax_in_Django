FROM python:3.7-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 USE_MOCKS=1 DJANGO_ALLOWED_HOSTS=*
WORKDIR /app
COPY requirements-min.txt ./
RUN pip install --no-cache-dir -r requirements-min.txt
COPY . .
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
