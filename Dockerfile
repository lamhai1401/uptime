FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8080:8080

RUN python3 -m pip install --upgrade pip


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip3 install -r ./requirements/prod.txt

CMD [ "sh", "./entrypoint.sh" ]
