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

 Important
 [https://docs.wagtail.org/en/v7.2.1/advanced_topics/customization/custom_user_models.html]

 ```bash
 python manage.py makemigrations
 python manage.py migrate 
 ```

 ## 05 Setting up allauth in Django

 [https://pythoneatstail.com/en/overview-all-articles/set-allauth-django-project/]

 ```bash
 pip install django-allauth
 ```

## 06 Setting up validated login with allauth in Django

[https://pythoneatstail.com/en/overview-all-articles/setting-login-allauth-django/]

```bash
pip install django-widget-tweaks
```

## 07 Github, secret keys and other local settings

[https://pythoneatstail.com/en/overview-all-articles/github-secret-keys-and-other-local-settings/]

```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
# Put secret key in local.py
```

## 08 Signup and password reset with allauth's email verification in Django

[https://pythoneatstail.com/en/overview-all-articles/signup-and-password-reset-email-verification-allauth-django/]

```bash
```

## 09 Allowing users to update and delete their profile

[https://pythoneatstail.com/en/overview-all-articles/allowing-users-update-and-delete-their-profile/]

```bash
```

## 10 New base.html template

```bash
```

## 11 Relocate scoring app

```bash
# Relocate scoring app from newarcheryscoring to ..
# Create recording app in newarcheryscoring
python manage.py startapp scoring
cd newarcheryscoring
python ..\manage.py startapp recording
cd ..
```

## 12 Create scoring models, serializers and views

```
urls
http://localhost:8000/scoring/archers/
http://localhost:8000/scoring/disciplines/
http://localhost:8000/scoring/disciplinememberships/
http://localhost:8000/scoring/clubs/
http://localhost:8000/scoring/clubmemberships/
http://localhost:8000/scoring/categories/
http://localhost:8000/scoring/agegroups/
http://localhost:8000/scoring/teams/
http://localhost:8000/scoring/teammemberships/
http://localhost:8000/scoring/scoringsheets/
http://localhost:8000/scoring/targetfacenamechoices/
http://localhost:8000/scoring/targetfaces/
http://localhost:8000/scoring/rounds/
http://localhost:8000/scoring/roundmemberships/
http://localhost:8000/scoring/competitions/
http://localhost:8000/scoring/competitionmemberships/
```

```bash
python manage.py load_initial_data
python manage.py runserver
Part 3
serializers ..InfoSerializer classes completed
```

## 13 django-silk for Profiling and Optimization with Django REST Framework
 [https://www.youtube.com/watch?v=OG8alXR4bEs&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=5]

 ```bash
 pip install django-silk
 python manage.py makemigrations
 python manage.py migrate
 python manage.py collectstatic
 python manage.py runserver

 ```

## 14 Django REST Framework - Generic Views | ListAPIView & RetrieveAPIView

[https://www.youtube.com/watch?v=vExjSChWPWg&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=6]

```
```

```bash
del db.sqlite3
pyclean .
python manage.py makemigrations
python manage.py migrate
python manage.py load_initial_data
python manage.py runserver
```

## 15 Django REST Framework - Permissions and Testing Permissions

[https://www.youtube.com/watch?v=rx5IV_4Iuog&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=8]

```
```

```bash
python manage.py test scoring
```

## 16 Django REST Framework - APIView class

[https://www.youtube.com/watch?v=TVFCU0w65Ak&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=9]
[https://testdriven.io/blog/drf-views-part-2/]

```
```

```bash
```

## 17 Django REST Framework - Creating Data | ListCreateAPIView and Generic View Internals

[https://www.youtube.com/watch?v=Jh85U1nhMh8&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=10]

```
```

```bash
```

## 18 Django REST Framework - Customising permissions in Generic Views | VSCode REST Client extension

[https://www.youtube.com/watch?v=mlQZ1i8rUKQ&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=11]

```
```

```bash
```

## 19 Django REST Framework - JWT Authentication with djangorestframework-simplejwt

[https://www.youtube.com/watch?v=Xp0-Yy5ow5k&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=12]
[https://www.django-rest-framework.org/api-guide/authentication/#authentication]
[https://github.com/jazzband/djangorestframework-simplejwt]
[https://django-rest-framework-simplejwt.readthedocs.io/en/latest/]

```
```

```bash
pip install djangorestframework-simplejwt
```

## 20 Django REST Framework - Refresh Tokens & JWT Authentication

[https://www.youtube.com/watch?v=H3OY36wa7Cs&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=13]

```
```

```bash
```

## 21 Django REST Framework - Updating & Deleting data

[https://www.youtube.com/watch?v=08gHVFPFuBU&list=PL-2EBeDYMIbTLulc9FSoAXhbmXpLq2l5t&index=14]

```
```

```bash
```

## 22 drf-spectacular - Django REST Framework API Documentation

```
```

```bash
```

## 23 scoring app create wagtail page models

```
```

```bash
```

## 24 Advanced Wagtail Interfaces with Panel Types (and Orderables!)

```
```

```bash
```

## 25 Initial commit - Set TODO classes

```
```

```bash
```

## 26 Page permissions

```
```

```bash
```

## 27 Cache

```
```

```bash
```

## 28 Supercharging Wagtail Snippets with Advanced Features

```
Part1 Not finished yet
```

```bash
python manage.py update_index
```

## 29 Adding grid app

```
Part 1
```

```bash
python manage.py startapp my_grid_model
```

