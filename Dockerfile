# Gunakan Python 3.12 slim sebagai base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (untuk kompilasi kalau perlu)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt dulu (untuk caching layer)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir python-dotenv

# Copy seluruh project
COPY . .

# Buat folder uploads kalau belum ada
RUN mkdir -p app/static/uploads

# Expose port 5000 (port Flask)
EXPOSE 5000

# Set environment variable
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Jalankan aplikasi
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]