FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && export AIRFLOW_HOME=/app/airflow_home \
    && airflow db init

CMD ["python", "app.py"]
