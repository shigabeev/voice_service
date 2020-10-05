FROM python:3.7-slim-buster

MAINTAINER @NetBUG

RUN mkdir -p /apps/voice-service

COPY ./ /apps/voice-service

RUN pip3 install -r /apps/voice-service/requirements.txt

EXPOSE 4000

CMD [ "python3", "/apps/voice-service/web/backend.py" ]