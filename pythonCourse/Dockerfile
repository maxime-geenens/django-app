FROM ubuntu:20.04

# Install required packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends python3 \
    python3-pip \
    python3-setuptools \
    python3-pytest

# Set environment variables
ENV DockerHOME=/home/app/webapp
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p ${DockerHOME}
WORKDIR ${DockerHOME}

COPY . ${DockerHOME}

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

ENTRYPOINT ["/home/app/webapp/run.sh"]