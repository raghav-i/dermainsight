# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
