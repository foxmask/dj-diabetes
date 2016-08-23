from setuptools import setup, find_packages
from dj_diabetes import __version__ as version
import os


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))

install_requires = reqs('requirements.txt')

setup(
    name='dj_diabetes',
    version=version,
    description='Django Diabetes is a personal Glucose Manager',
    author='FoxMaSk',
    author_email='foxmask@trigger-happy.eu',
    url='https://github.com/foxmask/dj-diabetes',
    download_url="https://github.com/foxmask/dj-diabetes/"
                 "archive/dj-diabetes-" + version + ".zip",
    packages=find_packages(exclude=['dj_diabetes/local_settings']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
    install_requires=install_requires,
    include_package_data=True,
)
