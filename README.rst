.. image:: https://codeclimate.com/github/foxmask/dj-diabetes/badges/gpa.svg
    :target: https://codeclimate.com/github/foxmask/dj-diabetes
    :alt: Code Climate


.. image:: https://travis-ci.org/foxmask/dj-diabetes.svg?branch=master
    :target: https://travis-ci.org/foxmask/dj-diabetes
    :alt: Travis Status


.. image:: http://img.shields.io/pypi/v/dj-diabetes.svg
    :target: https://pypi.python.org/pypi/dj-diabetes/
    :alt: Latest version


.. image:: http://img.shields.io/badge/python-3.4-orange.svg
    :target: https://pypi.python.org/pypi/dj-diabetes/
    :alt: Python version supported


.. image:: http://img.shields.io/badge/license-BSD-blue.svg
    :target: https://pypi.python.org/pypi/dj-diabetes/
    :alt: License


.. image:: http://img.shields.io/pypi/dm/dj-diabetes.svg
   :target: https://pypi.python.org/pypi/dj-diabetes/
   :alt: Downloads per month


=================
 Django Diabetes
=================

Django Diabetes is a personnal Glucose Manager

It permits to follow your daily health


requirements:
=============

* Python 3.4
* Django 1.9
* arrow 0.6.0


Installation:
=============

to get the project, from your virtualenv, do :

.. code:: system

    git clone https://github.com/foxmask/dj-diabetes.git

to add the needed modules , do :

.. code:: python

    pip install -r requirements.txt

and at least :

.. code:: python

    python manage.py makemigrations dj_diabetes
    python manage.py migrate dj_diabetes
    python manage.py loaddata dj_diabetes_preferences.json

to startup the database and load the data



.. image:: http://foxmask.trigger-happy.eu/static/2014/06/glucose_manager-1024x771.png
