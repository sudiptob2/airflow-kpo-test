from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

dag = DAG('minimal_test_fail_task_without_cr', start_date=datetime(2022, 1, 1), schedule_interval='@once', catchup=False)

task = KubernetesPodOperator(
    task_id='minimal_test_fail_task_without_cr',
    image="alpine:latest",
    dag=dag,
    cmds=["/bin/sh", "-c", "-x"],
    arguments=["eccho", "Hello World!"],   # purposeful typo,
    log_events_on_failure=True,
)
