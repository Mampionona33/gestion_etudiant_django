FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt

RUN apt-get -y update

RUN apt-get install -y sqlite3 libsqlite3-dev

COPY . .

EXPOSE 8000