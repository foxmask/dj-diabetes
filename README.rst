===========
 Django Diabetes
===========

Django Diabetes is a personnal Glucose Manager

It permits to follow your daily health


requirements:
=========
* Python 2.7.x
* Django >= 1.6.5


Installation:
=============
to get the project, from your virtualenv, do :

.. code: system

    git clone https://github.com/foxmask/dj-diabetes.git

to add the needed modules , do :

.. code:: python

    pip install -r requirements.txt

and at least :

.. code:: python

    python manage.py syncdb
    python manage.py loaddata dj_diabetes_preferences.json

to startup the database and load the data

