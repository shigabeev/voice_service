FROM python:3.7-slim-buster

MAINTAINER @NetBUG

#install and source ansible
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-numpy \
    python3-matplotlib \
    python3-soundfile

RUN mkdir -p /apps/voice-service

COPY ./ /apps/voice-service

RUN pip3 install -r /apps/voice-service/requirements.txt

EXPOSE 4000

CMD [ "python3", "/apps/voice-service/src/backend.py" ]