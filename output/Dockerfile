```Dockerfile
# Use a small and secure base image
FROM tiangolo/ui:latest

# Add WORKDIR
WORKDIR /app

# Copy only required files
COPY . .

# Expose the port used by the app (8000)
EXPOSE 8000

# Use gunicorn as the GUNICORN_CMD_ARGS for runserver can use the PORT environment variable
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app"]
```

Assumptions:
- The FastAPI application is structured under a folder named `app`.
- There is a file named `main.py` that contains the entry point of your FastAPI app.
- You are using gunicorn for running the application, as it's common in production environments to use gunicorn with FastAPI.

Make sure your application and dependencies are set up correctly before building the Docker image.