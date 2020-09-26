# fullthrottle user_activity project

## setup virtualenv

```sh
pip install virtualenv
virtualenv .venv
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
