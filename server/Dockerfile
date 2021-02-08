# Import the base image
FROM python:3.9.1-slim

LABEL maintainer="Swathi M Ravindranath" \
    name="simple_autobot" \
    version="0.3"

WORKDIR /server

# the only requirement is requests
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED = 1

COPY . /server/

CMD ["python","./server.py"]