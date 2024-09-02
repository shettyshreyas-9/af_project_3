import os
import subprocess
import platform
import sys

def run_docker_compose():
    try:
        # Execute the docker-compose up --build command
        subprocess.run(["docker-compose", "up",'--build'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute docker-compose: {e}")

if __name__ == "__main__":
    run_docker_compose()
