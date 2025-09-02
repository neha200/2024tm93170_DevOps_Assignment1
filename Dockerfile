FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

# Install deps first (layer cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole repo (includes App/ and Test/)
COPY . .

EXPOSE 8000
# Run the Flask API (NOT the Tkinter app)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "App.flask_api:app"]
