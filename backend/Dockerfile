FROM ubuntu:latest
LABEL authors="eithelgonzalez"

ENTRYPOINT ["top", "-b"]

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV PYTHONPATH=/app
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]