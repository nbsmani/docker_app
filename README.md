# Docker ETL Pipeline
A data engineering pipeline using Docker Compose to process CSV data and store results in Postgres.

## Setup
- `Dockerfile`: Builds `etl` image.
- `docker-compose.yml`: Runs `app` (ETL) and `postgres` services.
- `process_data.py`: Processes CSV, computes the average (stored in means variable)  and pushes to `/app/output/output.csv` and Postgres `means` table.

## Run
```bash
docker build -t etl .
docker-compose up -d
docker exec -it my-data-app-postgres-1 psql -U balu -d mydata -c "SELECT * FROM means;"