# Docker ETL Pipeline
A data engineering pipeline using Docker Compose to process CSV data and store results in Postgres.
This version includes a streamlit dashboard.
## Setup
- `Dockerfile`: Builds `etl` image.
- `docker-compose.yml`: Runs `app` (ETL) and `postgres` services.
- `process_data.py`: Processes CSV, computes the average (stored in means variable)  and saves means to `/app/output/batch1_output.csv`, `/app/output/batch2_output.csv`, and Postgres batch1_means, batch2_means” to reflect scaling
- `dashboard.py`: Connects to the postgres service and display the batch1_means table in the web app. 
## Run
```bash
docker build -t etl .
docker-compose up -d
```

## Result
The dashboard can be accessed at http://0.0.0.0:8501/ in a web browser.
