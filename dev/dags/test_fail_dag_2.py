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

dag = DAG('test_fail_dag_2',
          default_args=default_args,
          description='A simple dag that uses the KubernetesPodOperator and fails on runtime',
          schedule_interval='@once',
          catchup=False)

resource_reqs = {
    'requests': {
        'memory': '100Mi',
    },
    'limits': {
        'memory': '200Mi',
    },
}

simple_task = KubernetesPodOperator(
    task_id='test_fail_task_2',
    name='test_fail_task_2',
    image='bad_image_sudiptob2:latest',
    container_resources=resource_reqs,
    log_events_on_failure=True,
    dag=dag
)
simple_task
