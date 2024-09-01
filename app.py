import os
import subprocess

def start_airflow():
    # Set the environment variable for Airflow home
    os.environ['AIRFLOW_HOME'] = os.path.join(os.getcwd(), 'airflow_home')
    
    # Initialize the Airflow database
    subprocess.run(["airflow", "db", "init"])
    
    # Start the Airflow web server
    webserver = subprocess.Popen(["airflow", "webserver"])
    
    # Start the Airflow scheduler
    scheduler = subprocess.Popen(["airflow", "scheduler"])
    
    return webserver, scheduler

if __name__ == "__main__":
    webserver, scheduler = start_airflow()
    
    try:
        # Keep the script running to keep the processes alive
        webserver.wait()
        scheduler.wait()
    except KeyboardInterrupt:
        # Gracefully stop the processes on exit
        webserver.terminate()
        scheduler.terminate()
