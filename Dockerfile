FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# системные зависимости для psycopg (бинарный пакет без компиляции)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

# Вариант 1: requirements.txt
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Вариант 2: pyproject+poetry (если используете Poetry) — закомментируйте/настройте при необходимости
# RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY . /app

EXPOSE 8000
CMD ["sh", "entrypoint.sh"]
