FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app
RUN apt-get update -y && apt install -y netcat iputils-ping traceroute
RUN mkdir /app
WORKDIR /app

COPY . /app
RUN mkdir /app/staticfiles
RUN mkdir /app/mediafiles
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN chmod +x /app/scripts/prestart.sh
RUN chmod +x /app/scripts/run_dev.sh
RUN chmod +x /app/scripts/run_prod.sh
