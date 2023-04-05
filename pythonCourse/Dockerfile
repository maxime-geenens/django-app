FROM python:3.10.5

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