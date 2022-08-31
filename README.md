# Epic-Event-v1
***
Api for secure internal CRM system..

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Run the project](#run-the-project)
5. [Admin](#django-admin)
6. [Access and Documentation](#access-and-documentation)

## General Info
***

## Technologies
***
* [Python](https://example.com): Version 3.9.6
* [Django](https://www.djangoproject.com/): Version 4.0.1
* [Django REST](https://www.django-rest-framework.org/): Version 3.12.4

## Installation
***

A little intro about the installation.

Clone the project-repository, and go to the project-folder.
```
$ git clone https://github.com/MarineBdlt/Soft-Desk-v2.git
$ cd ./Soft-Desk-v2
```

Set up your environnement and install the requirements.
```
$ python -m venv env
```
To activate the environment, run source env/bin/activate (if you are on Windows, the command will be env/Scripts/activate.bat ). 
```
~/Soft-Desk-v2/$ source env/bin/activate
(env) ~/epicevent$
```

The following command will install the packages according to the configuration file requirements.txt.
```
$ pip install -r requirements.txt
```

## Run the project

Write  the following line in the console to run the web server.
```
$ python manage.py runserver 
```
You can find the app on django-host : http://127.0.0.1:8000/

## Access and Documentation

Go to your browser and type the address http://127.0.0.1:8000/api/login.
Check the [POSTMAN DOCUMENTATION](https://documenter.getpostman.com/view/16475012/VUqoPJD9) of Epic Event API

## Django admin

Go to your browser and type the address http://127.0.0.1:8000/admin/.

If you want to know more about Django admin, you should check Django's documentation: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/


