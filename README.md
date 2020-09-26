# fullthrottle user_activity project

## setup venv

```sh
python3 -m venv venv
```

## install requirements

```bash
pip install -r requirements.txt

```

## running django management commands & usage

```sh
source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=useractivity.settings
python manage.py build -a mini_projects
python manage.py makemigrations
python manage.py migrate
python manage.py load_activity_data
python manage.py runserver
```

# to GET the user activity data go to api/users/activities/
