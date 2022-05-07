from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta

default_args = {
    'owner': '10Academy',
    'depends_on_past': False,
    'start_date': datetime(2021, 9, 23),
    'email': ['danielzelalemheru@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
dag = DAG(
    'dbt_dag',
    default_args=default_args,
    description='An Airflow DAG to invoke simple dbt commands',
    schedule_interval='@once',
    # schedule_interval='*/1 * * * *'
)

dbt_debug = BashOperator(
    task_id='dbt_debug',
    bash_command='cd /dbt && dbt debug',
    dag=dag
)

dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='cd /dbt && dbt run',
    dag=dag
)

dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='pwd',
    dag=dag
)

docs = BashOperator(
    task_id='documentation',
    bash_command='cd /dbt && dbt docs generate',
    dag=dag
)

dbt_debug >> dbt_run >> dbt_test
dbt_run >> docs