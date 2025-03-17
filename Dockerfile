FROM python:3.9 AS backend-builder
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends build-essential
RUN pip install --no-cache-dir -r requirements.txt
FROM python:3.9.21-slim
WORKDIR /app
COPY --from=backend-builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY script.py .
#CMD ["/bin/bash", "script.py", "main:app"]
CMD ["python", "/app/script.py"]