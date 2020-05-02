# IMISCloud
Cloud

# Cloud Storage
Store/View Image/Music/Video/Files

# Commands
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Deploy
heroku run python manage.py makemigrations --app=imiscloud
heroku run python manage.py migrate --app=imiscloud
heroku run python manage.py createsuperuser --app=imiscloud