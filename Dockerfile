FROM python:2.7.14-stretch
FROM ubuntu:latest
MAINTAINER Kalab Oster
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /stringer
WORKDIR /stringer
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["permutations_app.py"]