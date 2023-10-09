FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY *.py .
COPY requirements.txt .
COPY names.sql .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]