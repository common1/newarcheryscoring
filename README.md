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

