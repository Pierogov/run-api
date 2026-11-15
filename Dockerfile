FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir "Flask>=3.1,<4"

COPY app.py .
COPY times/ ./times/

VOLUME ["/app/times"]
EXPOSE 5000

CMD ["python", "app.py"]
