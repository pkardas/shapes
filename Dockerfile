FROM python:3.8.2

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache -r requirements.txt

ADD . /usr/src/app

ARG GIT_SHA=none
ENV GIT_SHA=$GIT_SHA
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
