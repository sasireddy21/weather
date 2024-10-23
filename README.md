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


# Weather API Instructions

## Check Weather History
You can check the weather history using the following endpoints:

- Retrieve the weather history:
  ```plaintext
  http://127.0.0.1:8000/api/weather?limit=10
  ```
  <img width="952" alt="Weather full data" src="https://github.com/user-attachments/assets/29cce954-7d92-455d-83fb-b24603ed70ec">


- Retrieve the records for a specific station:
  ```plaintext
  http://127.0.0.1:8000/api/weather?limit=10&station_id=USC00257715
  ```

- Retrieve records for a specific date at a specific station:
  ```plaintext
  http://127.0.0.1:8000/api/weather?limit=10&station_id=USC00257715&date=1985-01-01
  ```

## Check Stats History
You can check the stats history using the following endpoints:

- Retrieve stats for a specific station:
  ```plaintext
  http://127.0.0.1:8000/api/weather/stats?station_id=USC00110187
  ```

- Retrieve stats for a specific station for a specific year:
  ```plaintext
  http://127.0.0.1:8000/api/weather/stats?station_id=USC00110187&year=1985
  ```

- Retrieve stats for a specific year:
  ```plaintext
  http://127.0.0.1:8000/api/weather/stats?year=1985
  ```

