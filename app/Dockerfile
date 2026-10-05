# 1) Base image: python:3.12-alpine (~50 MB) instead of python:3.12 (~1 GB)
FROM python:3.12-alpine

# 2) Do not write .pyc files and print logs immediately
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 3) Create a normal user so the app does not run as root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 4) Copy requirements first: this layer stays in cache
#    as long as requirements.txt does not change
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copy the source code last (it changes often)
COPY app.py .

# 6) Switch to the non-root user
USER appuser

EXPOSE 5000

# 7) Command executed when the container starts
CMD ["python", "app.py"]
