FROM python:3.9-slim-buster

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir Flask
COPY . .

EXPOSE 5000

CMD ["python","app.py"]

