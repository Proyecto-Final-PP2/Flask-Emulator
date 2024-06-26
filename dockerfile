FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY templates templates
COPY static static


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
