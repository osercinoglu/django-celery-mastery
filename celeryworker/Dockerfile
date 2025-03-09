FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Ensure Python output is sent directly to the terminal
# without buffering.
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app/