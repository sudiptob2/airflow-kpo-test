FROM --platform=linux/amd64 apache/airflow:2.8.1-python3.8 as build

USER airflow
# Airflow user in Docker image version 2.2.0+ moved to root group to be compatible with Open-Shift (https://airflow.apache.org/docs/docker-stack/entrypoint.html#allowing-arbitrary-user-to-run-the-container),
# below COPY is from official example: https://airflow.apache.org/docs/docker-stack/build.html#example-when-you-want-to-embed-dags
COPY --chown=airflow:root dags /opt/airflow/dags