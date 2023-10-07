# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your Flask app will run on
EXPOSE 5000

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Command to run your application
CMD ["python", "src/api.py"]
