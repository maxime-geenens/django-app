#!/bin/sh

python manage.py makemigrations
python manage.py makemigrations courses
python manage.py migrate

python manage.py loaddata init-data.yaml

echo ">>> Create users"
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').count() or User.objects.create_superuser('admin', 'test@test.com', 'admin!')" | python manage.py shell
#echo "from django.contrib.auth.models import User; User.objects.filter(username='MTOUZI-EXTERNAL@scor.com').count() and User.objects.filter(username='MTOUZI-EXTERNAL@scor.com').update(is_superuser=True, is_staff=True)" | python3.8 manage.py shell

exec "$@"