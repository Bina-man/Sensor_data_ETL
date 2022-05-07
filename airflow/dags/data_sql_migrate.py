from redash_toolbelt.client import Redash

from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator



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

def migrate_sql_statemtents(**kwargs):
  src_path = kwargs['src_path']
  tgt_path = kwargs['tgt_path']
  mysql_converter.convert_create_statements(src_path, tgt_path)


dag = DAG(
    'sql_migration',
    default_args=default_args,
    description='An Airflow DAG to export sql statements',
    schedule_interval='@once',
    # schedule_interval='*/ * * * *'
)


export_sql_statments = PythonOperator(
    task_id='export_sql_statments',
    python_callable=migrate_sql_statemtents,
    op_kwargs={'src_path':  "/airflow/dags/mysqlSql/", 'tgt_path': "/airflow/dags/postgresSql/"},
    dag=dag
)