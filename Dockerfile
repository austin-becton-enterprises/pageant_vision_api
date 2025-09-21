# Final, Best-Practice Dockerfile

# Use a specific, stable Python version
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Prevent Python from writing .pyc files and ensure output is sent straight to the terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a non-privileged user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Copy requirements file first to leverage Docker's layer caching.
# If requirements.txt doesn't change, this layer won't be rebuilt.
COPY requirements.txt .
COPY hax_packages ./hax_packages
# Install dependencies as root to ensure they are in the system PATH
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code into the container
COPY . .

# Change ownership of the application directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-privileged user to run the application
USER appuser

# Let Cloud Run set the PORT. Default to 8080 for local testing.
ENV PORT 8080

# Use the shell form of CMD to correctly expand the $PORT environment variable.
# This is the standard and correct way to handle dynamic variables in the start command.
CMD ["/bin/sh", "-c", "gunicorn --bind 0.0.0.0:$PORT --workers 2 --worker-class uvicorn.workers.UvicornWorker main:app"]
