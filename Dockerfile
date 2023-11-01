
# Use an official Python runtime as a parent image
FROM python:3.11

# set enviroment Variable for image 
ENV PYTHONUNBUFFERED 1

# Set the working Directory in the container
WORKDIR /app

# Copy the requirements file into the container

COPY requirements.txt /app/


# Install any needed packages specified in requirements.txt

RUN pip install -r requirements.txt

# Copy The rest of your application's code into the container

COPY . /app/

# Expose the port on which your Django app will run (e.g., 8000)
EXPOSE 8000

# Define the command to start your Django application

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
