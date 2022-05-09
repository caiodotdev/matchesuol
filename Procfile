release: python manage.py migrate

web: gunicorn matches.wsgi --log-file -

worker: celery -A app beat -l info && celery -A app worker -l INFO -c 1

