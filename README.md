# Project Instructions

## Running Migrations
Run the following commands to apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Dump Data into SQLite Database
To dump the data from the `wx_data` folder into the SQLite database, use:
```bash
python manage.py dumpintodb
```

## Calculate the Temperature
To calculate the temperature, run:
```bash
python manage.py analysis
```

## Run Unit Test Cases
To check the weather analysis table with unit tests, execute:
```bash
python manage.py test
```

## Run the Server
To start the server, use:
```bash
python manage.py runserver
```
