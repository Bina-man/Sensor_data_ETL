from redash_toolbelt.client import Redash

from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator

from airflow.operators.bash_operator import BashOperator

import sys
sys.path.insert(0,"/airflow/dags/scripts")
import scripts.redash_export_query as redash_export_query


redash_api = 'F23HKin8rRi9nNmuf7m20X2QFqvmv93atp8BKZ9c'
redash_url = 'http://localhost:5000'



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

template = u"""/*
Name: {name}
Data source: {data_source}
Created By: {created_by}
Last Updated At: {last_updated_at}
*/
{query}"""

dag = DAG(
    'export_redash_query',
    default_args=default_args,
    description='An Airflow DAG to export redash query',
    schedule_interval='@once',
    # schedule_interval='*/ * * * *'
)


export_redash_data = BashOperator(
    task_id='export_redash_data',
    bash_command='python3 /airflow/dags/scripts/redash_export_query.py',
    dag=dag
)