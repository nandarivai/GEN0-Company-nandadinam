FROM python:3.10-slim

# 1. Install dependencies dulu
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 2. Siapkan working dir dan install Python lib
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy source code
COPY . /app

EXPOSE 5000
CMD ["python", "app.py"]
