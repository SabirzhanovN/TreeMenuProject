# How to use

> Clone this repository
```commandline
$ git clone git@github.com:SabirzhanovN/TreeMenuProject.git 
```

***
>Activate your venv
~~~~
$ cd TreeMenuProject
$ python3 -m venv venv
$ source venv/bin/activate 
~~~~

> Install requirements
```commandline
$ pip install -r requirements.txt
```

> Make and migrate models
```
$ python manage.py makemigrations
$ python manage.py migrate 
```

> Create admin(superuser)

``` 
$ python manage.py createsuperuser 
```

> Run this project
```commandline
$ python manage.py runserver
```
