FROM python:3.9-slim-bookworm as builder

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED=1

# Virtual environment
ENV VIRTUAL_ENV=/opt/venv

# dependencies
RUN apt-get update

# Create virtual environment
RUN python3 -m venv $VIRTUAL_ENV

# Activate virtual environment
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir --upgrade -r requirements.txt

COPY ./src /app/src
