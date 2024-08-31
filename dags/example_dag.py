from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from google.cloud import bigquery
from datetime import datetime

def query_gbq(**kwargs):
    # Set up BigQuery client
    client = bigquery.Client()
    
    # Query to be executed
    query = """
    SELECT * FROM `your_project.your_dataset.your_table`
    LIMIT 1000
    """
    
    # Perform the query
    query_job = client.query(query)
    
    # Fetch the results
    results = query_job.result()
    
    for row in results:
        print(row)

# Define default arguments
default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

# Define the DAG
with DAG(
    'gbq_query_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    # Define the tasks
    run_query = PythonOperator(
        task_id='query_gbq_task',
        python_callable=query_gbq,
        provide_context=True
    )

    run_query
