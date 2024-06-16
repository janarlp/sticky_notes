# Sticky Notes App

To run the application.

`python3 manage.py runserver`

### Running Tests

`python3 manage.py test task_manager`

### Database Migration

1) Create a back up of database. 
2) Copy the code onto the server and run.
```
python manage.py makemigrations

python manage.py migrate
```

3) Migrate the data to the server as a copy