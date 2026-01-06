# newarcheryscoring

## See also

[https://docs.wagtail.org/en/stable/getting_started/tutorial.html]

## 00 Create virtual environment

``` bash
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# Linux
source .venv/bin/activate
```

## 01 Create Wagtail Project + apps

```bash
pip install wagtail
cd newarcheryscoring
wagtail start newarcheryscoring .
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

python manage.py startapp userauth
cd newarcheryscoring
python ..\manage.py startapp base
python ..\manage.py startapp blog
python ..\manage.py startapp locations
python ..\manage.py startapp people
python ..\manage.py startapp scoring
```

## 02 Wagtail with a custom user model

[https://pythoneatstail.com/en/overview-all-articles/wagtail-custom-user-model/]

```bash
python manage.py makemigrations
python manage.py runserver
```

## 03 Create fill_db app

```bash
pip install pyclean
python manage.py startapp fill_db

del db.sqlite3
pyclean .
python manage.py makemigrations
python manage.py migrate
python manage.py load_initial_data
python manage.py runserver
```
 ## 04 Adding extra fields to a Django custom user model

 [https://pythoneatstail.com/en/overview-all-articles/add-extra-fields-custom-user-model/]

 ```bash
 python manage.py makemigrations
 python manage.py migrate 
 ```

 