# Procfile

release: python manage.py db upgrade
web: gunicorn wsgi:app --access-logfile=-

