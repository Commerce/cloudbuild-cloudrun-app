# Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080 # Cloud Run typically uses PORT env var, but EXPOSE is good practice

CMD ["python", "app.py"]
