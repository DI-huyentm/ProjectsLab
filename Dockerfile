# Use the official Python base image
FROM python:3.9

# Set a working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Command to run when the container starts
CMD ["python", "main.py"]
