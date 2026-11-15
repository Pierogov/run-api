FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir "Flask>=3.1,<4" gunicorn

COPY app.py .
COPY times/ ./times/

VOLUME ["/app/times"]
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "app:app"]
