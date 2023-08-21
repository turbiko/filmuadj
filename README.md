Service for film.ua site inserted as zakupivli link 

Installation procedure
```bash

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  
python manage.py createsuperuser --email user@mail.tld --username username  
python manage.py runserver 127.0.0.1:8010
```