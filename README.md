[![Code Climate](https://codeclimate.com/github/push-things/dj-diabetes/badges/gpa.svg)](https://codeclimate.com/github/push-things/dj-diabetes) [![Test Coverage](https://coveralls.io/repos/github/push-things/dj-diabetes/badge.svg)](https://coveralls.io/github/push-things/dj-diabetes) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/push-things/dj-diabetes/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/push-things/dj-diabetes/?branch=master) [![Travis Status](https://travis-ci.org/push-things/dj-diabetes.svg?branch=master)](https://travis-ci.org/push-things/dj-diabetes) [![Latest version](http://img.shields.io/pypi/v/dj-diabetes.svg)](https://pypi.org/pypi/dj-diabetes/) [![Python version supported](http://img.shields.io/badge/python-3.6-orange.svg)](https://pypi.org/pypi/dj-diabetes/) [![License](http://img.shields.io/badge/license-BSD-blue.svg)](https://pypi.python.org/pypi/dj-diabetes/)

Django Diabetes
===============

Django Diabetes is a personal Glucose Manager

It allows you to follow your daily health

Improvements
------------

As I'm not suffering from diabetes, I am very open to suggestions for improvement of this project that I designed for a friend. For example with the type of examinations, etc... Currently I maintain the project by evolving versions of python and django.

Requirements:
-------------

-   Python 3.6
-   Django 2
-   arrow 0.12.x

Installation:
-------------

to get the project, from your virtualenv, do :

``` sourceCode
git clone https://github.com/push-things/dj-diabetes.git
```

to add the needed modules , do :

``` sourceCode
pip install -r requirements.txt
```

create a new user who will be the admin :

``` sourceCode
python manage.py createsuperuser
```

and at least :

``` sourceCode
python manage.py makemigrations dj_diabetes
python manage.py migrate dj_diabetes
python manage.py loaddata dj_diabetes_preferences.json
python manage.py createsuperuser
```

to startup the database and load the data

![image](https://foxmask.net/static/2014/06/glucose_manager-1024x771.png)
