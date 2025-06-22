FROM python:3.7

RUN apt-get update && apt-get install -y

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY network .

EXPOSE 8000
CMD ["python", "manage.py", "runsslserver", "0.0.0.0:8000", "--certificate", "/etc/ssl/cert.crt", "--key", "/etc/ssl/key.key"]
