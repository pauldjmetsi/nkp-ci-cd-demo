# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app/requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .

# Expose port and set env
ENV APP_VERSION=v1.0
EXPOSE 8080

CMD ["python", "app.py"]
