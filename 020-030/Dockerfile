FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install flask prometheus_client

EXPOSE 8080 8000
CMD ["python", "app.py"]
