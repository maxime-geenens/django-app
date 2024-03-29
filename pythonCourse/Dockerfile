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

# Install pip
RUN python3 -m pip install --upgrade pip

# Create and use virtual environment
RUN python3 -m pip install virtualenv && \
  virtualenv --version
RUN python3 -m virtualenv .venv &&\
  . .venv/bin/activate

# Copy app files to workdir
COPY ./pythonCourse ${DockerHOME}

# Install requirements
RUN python3 -m pip install -r requirements.txt

RUN python3 manage.py makemigrations && \
  python3 manage.py makemigrations courses && \
  python3 manage.py migrate && \
  python3 manage.py loaddata init-data.yaml && \
  echo ">>> Create users" && \
  echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').count() or User.objects.create_superuser('admin', 'test@test.com', 'admin!')" | python3 manage.py shell
