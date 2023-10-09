FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY main.py .
COPY template ./template
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]