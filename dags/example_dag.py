from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hello world!'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

with DAG('hello_world_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello)

