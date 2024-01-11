# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY ./app .

# Copy the python requirements
COPY requirements.txt .

# Install any needed packages specified in requirements.txt reducing the final image size preventing pip caching with "--no-cache-dir"
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Let's keep our service safe using a non-root user to run the application
RUN addgroup --system greetings && adduser --system --ingroup greetings greetings
USER greetings

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
