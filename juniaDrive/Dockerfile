# # Use an official Python runtime as a parent image
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run the Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


                                                                   # Use the official Python image
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install PostgreSQL client tools for pg_isready
RUN apt-get update && apt-get install -y postgresql-client

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the entrypoint script and grant execution permissions
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Copy the application code
COPY . /app/

# Run the entrypoint script by default
ENTRYPOINT ["/app/entrypoint.sh"]

# Run Django on 0.0.0.0:8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
