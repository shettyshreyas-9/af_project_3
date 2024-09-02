# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Docker CLI and docker-compose
RUN apt-get update && \
    apt-get install -y \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# Install docker-compose
RUN pip install --no-cache-dir docker-compose

# Copy the current directory contents into the container at /usr/src/app
COPY . .

EXPOSE 8080
# Make the container's default command be the Docker CLI
# CMD ["docker-compose", "--version"]
CMD ["python", "app.py"]