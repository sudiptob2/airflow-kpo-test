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

resource_reqs = {
    'requests': {
        'memory': '50Mi',
    },
    'limits': {
        'memory': '100Mi',
    },
}

simple_task = KubernetesPodOperator(
    namespace='default',
    task_id='test_fail_task',
    name='test_fail_task',
    cmds=['stress'],
    arguments=['--vm', '1', '--vm-bytes', '250M', '--vm-hang', '1', '--verbose'],
    image='polinux/stress',
    container_resources=resource_reqs,
    log_events_on_failure=True,
    dag=dag
)
simple_task
