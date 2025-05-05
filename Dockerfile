FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    git \
    && apt-get clean

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip \
    pip install -r /app/requirements.txt

CMD ["python", "main.py"]