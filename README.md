# weather

--run the migration
python manage.py makemigrations
python manage.py migrate 

--dump the data from wx_data folder into sqlite DB
python manage.py dumpintodb

--calculate the temperature
python manage.py analysis

--Unit test cases to check the weather analysis table
python manage.py test

--run the server
python manage.py runserver
