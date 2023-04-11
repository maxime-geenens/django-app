#!/bin/sh

python3 manage.py makemigrations
python3 manage.py makemigrations courses
python3 manage.py migrate

python3 manage.py loaddata init-data.yaml

echo ">>> Create users"
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').count() or User.objects.create_superuser('admin', 'test@test.com', 'admin!')" | python3 manage.py shell
#echo "from django.contrib.auth.models import User; User.objects.filter(username='MTOUZI-EXTERNAL@scor.com').count() and User.objects.filter(username='MTOUZI-EXTERNAL@scor.com').update(is_superuser=True, is_staff=True)" | python3.8 manage.py shell

exec "$@"