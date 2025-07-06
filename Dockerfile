FROM python:3.10-slim
WORKDIR /app
COPY backend /app
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "stock_prediction_main.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
