# Import the base image
FROM python:3.9.1-slim

WORKDIR /server

# the only requirement is requests
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED = 1

COPY . /server/

CMD ["python","./server.py"]