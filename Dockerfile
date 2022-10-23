FROM python:slim-bullseye

WORKDIR /app
COPY ./backend/.  /app

RUN apt update && apt install -y python3-pip

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir emails && \
    pip install  --no-cache-dir flask-restful

CMD ["python3", "-u", "/app/autoreply-backend.py"]

