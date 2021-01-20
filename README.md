# django-app
A base application with Django which can be extended further

## IDE used
 Pycharm
 
## Database
 * SQLite  
 * PGSql
   - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
   - pip install psycopg2
   - pip install psycopg2-binary
   - Configuration for Django settings
     
     ```
       DATABASES = {
        'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'dapp',
          'USER': 'postgres',
          'PASSWORD': 'postgres',
          'HOST': 'localhost'
         }
       }
     ```
     
 ## Libraries
 - [Django Stores](https://github.com/jschneier/django-storages)
 
 ## Working of Django forms
 ![Django forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms/form_handling_-_standard.png)
 
 ## Samples
  - https://github.com/sibtc/django-upload-example
  - [Datatables](https://github.com/theyogicoderRI/DjangoInchByInch)
