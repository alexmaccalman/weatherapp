# Use an official Python runtime as a parent image
FROM python

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=server.py

# Expose port 5001 for Flask
EXPOSE 5001

# Run the command to start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]