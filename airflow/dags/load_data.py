from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from airflow.operators.mysql_operator import MySqlOperator
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
    'data_load_dag',
    default_args=default_args,
    description='An Airflow DAG to invoke simple dbt commands',
    schedule_interval='@once',
    # schedule_interval='*/ * * * *'
)


create_statation_mysql_task = MySqlOperator(
    task_id='create_satations',
    mysql_conn_id='mysql_conn_id',
    sql='./mysqlSql/create_stations.sql',
    dag=dag
)


load_statation = MySqlOperator(
    task_id='load_station_data',
    mysql_conn_id='mysql_conn_id',
    sql='./mysqlSql/insert_stations.sql',
    dag=dag
)

create_obs_table_mysql_task = MySqlOperator(
    task_id='raw_observations_creator',
    mysql_conn_id='mysql_conn_id',
    sql='./mysqlSql/create_table.sql',
    dag=dag
)


load_obs_data = MySqlOperator(
    task_id='raw_data_loader',
    mysql_conn_id='mysql_conn_id',
    sql='./mysqlSql/insert_obs.sql',
    dag=dag
)

create_station_summary_table_mysql_task = MySqlOperator(
    task_id='station_summary_creator',
    mysql_conn_id='mysql_conn_id',
    sql='./mysqlSql/create_station_summary_table.sql',
    dag=dag
)


load_station_summary_data = MySqlOperator(
    task_id='station_summary_loader',
    mysql_conn_id='mysql_conn_id',
    sql='./mysqlSql/insert_station_summary_data.sql',
    dag=dag
)


create_obs_table_mysql_task >> load_obs_data
create_statation_mysql_task >> load_statation
create_station_summary_table_mysql_task >> load_station_summary_data

