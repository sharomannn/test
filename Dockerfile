# Используем образ Python 3.10
FROM python:3.10.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt и устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в рабочую директорию
COPY . /app/

# Выполняем миграции и собираем статические файлы при сборке контейнера
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Команда для запуска Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "test.wsgi:application"]
