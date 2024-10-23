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


# ETL Tool with Django, SQLite, and AWS Services

## Overview

This project leverages **Django**, **SQLite**, and various **AWS services** to create a scalable, automated ETL pipeline with an API. Below is an outline of the tools and services used for different components of the architecture.

---

## Tools & AWS Services

| **Component**         | **AWS Service**               | **Purpose**                                                 |
|-----------------------|-------------------------------|-------------------------------------------------------------|
| **API Hosting**        | **AWS Elastic Beanstalk**      | For deploying and managing the Django REST API.              |
| **Database**           | **SQLite** (or **RDS**)        | SQLite for small databases; RDS for future scalability.      |
| **Data Ingestion**     | **AWS Lambda** + **EventBridge** | Automated ETL operations via serverless computing.           |
| **Static Files**       | **Amazon S3**                 | Storing and serving static assets like media, CSS, JS.       |
| **Monitoring & Logs**  | **AWS CloudWatch**            | Monitoring API health, performance, and ingest logs.         |

---

## Architecture Overview

1. **API Deployment and Hosting**: 
   - The Django REST API is deployed using **AWS Elastic Beanstalk** for easy scaling and managed infrastructure. It supports dynamic scaling and can handle increased traffic automatically.

2. **Database**: 
   - Initially using **SQLite** for lightweight, on-premise database needs. The database can be migrated to **Amazon RDS** for better scalability and multi-user support in a production environment.

3. **Data Ingestion**: 
   - **AWS Lambda** is used for the serverless ingestion of data, triggered by **Amazon EventBridge** on a scheduled basis for automated execution.

4. **Static File Storage**: 
   - Static files such as media, CSS, and JavaScript are stored and served through **Amazon S3**, providing scalability and reliability.

5. **Monitoring & Logging**:
   - Application monitoring is done using **AWS CloudWatch**, which tracks metrics, logs, and sets up alarms for potential issues.

---

## Future Considerations

- **Database Scaling**: As the data grows, migrate from **SQLite** to **Amazon RDS** for production-level database capabilities.
- **Auto Scaling**: Enable auto-scaling for **Elastic Beanstalk** to dynamically adjust resources based on traffic.
- **Advanced ETL**: If the data becomes more complex, consider leveraging **AWS Glue** for scalable, serverless ETL.

---

## How to Deploy

1. Deploy the Django API on **AWS Elastic Beanstalk** using the CLI or console.
2. Schedule data ingestion jobs using **AWS Lambda** and **EventBridge**.
3. Store static files in **Amazon S3** and configure Django to serve these files.
4. Monitor application performance and logs using **AWS CloudWatch**.

---

## License

This project is licensed under the MIT License.
