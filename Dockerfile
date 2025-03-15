# Start with an official Python image
FROM python:3.12
ENV PYTHONPATH="/app"
# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . /app/

# Set the entrypoint to run Flask
# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:app"]
# CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "5000"]
