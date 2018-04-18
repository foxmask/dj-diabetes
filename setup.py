from setuptools import setup, find_packages
from dj_diabetes import __version__ as version
import os


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))


def readme():
    with open('README.rst') as f:
        return f.read()


install_requires = reqs('requirements.txt')

setup(
    name='dj_diabetes',
    version=version,
    description='Django Diabetes is a personal Glucose Manager',
    long_description=readme(),
    author='FoxMaSk',
    maintainer='FoxMaSk',
    author_email='foxmask@trigger-happy.eu',
    maintainer_email='foxmask@trigger-happy.eu',
    url='https://github.com/push-things/dj-diabetes',
    download_url="https://github.com/push-things/dj-diabetes/"
                 "archive/dj-diabetes-" + version + ".zip",
    packages=find_packages(exclude=['dj_diabetes/local_settings']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Topic :: Database',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    install_requires=install_requires,
    include_package_data=True,
)
