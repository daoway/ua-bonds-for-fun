# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
#COPY . .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY bonds-ua.py .


# Make port 80 available to the world outside this container (optional if running a web server)
# EXPOSE 80

# Run bond_yield_calculator.py when the container launches
CMD ["python", "./bonds-ua.py"]
