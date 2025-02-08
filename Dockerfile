FROM python:3.10-slim-buster  

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port FastAPI listens on (default 8000)
EXPOSE 8000

# Use Uvicorn to run the FastAPI app.  CMD is what runs when the container starts.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]