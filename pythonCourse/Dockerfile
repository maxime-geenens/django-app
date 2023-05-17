FROM python:3.10.5

# Set environment variables
ENV DockerHOME=/home/app/webapp
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p ${DockerHOME}
WORKDIR ${DockerHOME}

# Install pip
RUN python3 -m pip install --upgrade pip

# Create and use virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files to workdir
COPY ./pythonCourse ${DockerHOME}

RUN python3 manage.py makemigrations && \
  python3 manage.py makemigrations courses && \
  python3 manage.py migrate && \
  python3 manage.py loaddata init-data.yaml && \
  echo ">>> Create users" && \
  echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').count() or User.objects.create_superuser('admin', 'test@test.com', 'admin!')" | python3 manage.py shell
