# Dockerfile
FROM python:3.8                       # Base image for our job
RUN pip install --upgrade pip && \
    pip install -U setuptools==49.6.0 # Upgrade pip and setuptools
RUN apt-get update && \
    apt-get install unzip groff -y    # Install few system dependencies
COPY requirements.txt ./              # Copy requirements.txt file into image
RUN pip install -r requirements.txt   # Installing project dependencies