* django-admin help  
* django-admin startproject project-name  
* python manage.py help
* Start server  
  - python mange.py runserver
* python mange.py startapp app-name
* python manage.py collectstatic
  - generates static folder with configured resources 
* Database tables creation
  
  - python manage.py makemigrations
    - creates intermediate migration files which is then used by 'migrate' command 
  - python manage.py sqlmigrate <appname> <filenumber>
    -  shows sql for the model creation    
  - python manage.py migrate
    - creates model in the connected database that is specified in settings.py