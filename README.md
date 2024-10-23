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
  <img width="953" alt="State_id" src="https://github.com/user-attachments/assets/695da1dd-e713-47a9-aebe-9379217e3764">


- Retrieve records for a specific date at a specific station:
  ```plaintext
  http://127.0.0.1:8000/api/weather?limit=10&station_id=USC00257715&date=1985-01-01
  ```
  <img width="949" alt="state_id and date" src="https://github.com/user-attachments/assets/1978286a-139d-4ab7-a566-0c1f389d9506">


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

  <img width="953" alt="station id analysis" src="https://github.com/user-attachments/assets/38ea31dd-a297-4576-b49e-1c22beb18629">


