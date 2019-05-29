# Use an official Python runtime as a parent image
FROM python:3.7.3

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "Script.py"]