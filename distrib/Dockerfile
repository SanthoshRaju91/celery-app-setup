FROM ubuntu:18.04

ENV HOME=/opt/repo

RUN apt-get update && apt-get install -y \
    build-essential \
    libsm6 \
    libxext6 \
    libxrender-dev \
    python3 \
    python3-pip

COPY ./src ${HOME}
COPY ./requirements.txt ${HOME}/requirements.txt

WORKDIR ${HOME}

RUN /usr/bin/pip3 install -r requirements.txt

COPY ./distrib/celeryd /etc/init.d/celeryd
COPY ./distrib/celery_config /etc/default/celeryd

RUN groupadd celery
RUN useradd celery -g celery

CMD ["/etc/init.d/celeryd", "start"]