# Dockerfile 
FROM python:3.9.17-bookworm

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True
# Copy local code to container image
ENV APP_HOME /back-end
WORKDIR $APP_HOME

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg

COPY . ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:app
