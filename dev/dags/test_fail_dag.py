from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'namespace': 'default',
    'image_pull_policy': 'Always'
}

dag = DAG('test_fail_dag',
          default_args=default_args,
          description='A simple dag that uses the KubernetesPodOperator and fails on runtime',
          schedule_interval='@once',
          catchup=False)

simple_task = KubernetesPodOperator(
    task_id='test_fail_task',
    name='test_fail_task',
    cmds=['python', '-c', 'raise Exception("This is a runtime failure")'], # This command will raise an exception.
    arguments=[],
    image='python:3.8-slim-buster',  # Use a Python image to execute Python commands
    log_events_on_failure=True,
    dag=dag
)

simple_task