FROM python:3.8-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    gcc \
    g++ \
    make \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sleep", "infinity"]