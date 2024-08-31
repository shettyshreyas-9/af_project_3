import os
from airflow import settings
from airflow.models import DagBag
from airflow.www.app import create_app

def run_airflow_webserver():
    # Initialize Airflow configuration
    os.environ['AIRFLOW_HOME'] = os.path.join(os.getcwd(), 'airflow_home')
    os.environ['AIRFLOW__CORE__LOAD_EXAMPLES'] = 'False'
    os.environ['AIRFLOW__WEBSERVER__WEB_SERVER_PORT'] = '8080'

    # Load the DAGs from the dags/ directory
    dag_bag = DagBag()

    # Create the web server app
    app = create_app()
    
    # Run the web server
    app.run(debug=True, port=8080)

if __name__ == "__main__":
    run_airflow_webserver()
