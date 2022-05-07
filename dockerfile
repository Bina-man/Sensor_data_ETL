FROM python:3.8
RUN pip install 'apache-airflow[postgres]==2.1.4' && pip install dbt
RUN pip install SQLAlchemy
RUN pip install apache-airflow-providers-postgres
RUN pip install apache-airflow-providers-mysql
RUN pip install dbt-mysql
RUN pip install mysql-connector-python
RUN pip install sqlalchemy
RUN pip install pymysql
RUN pip install pandas
RUN pip install redash_toolbelt

RUN mkdir /project
COPY scripts_airflow/ /project/scripts/

RUN chmod +x /project/scripts/init.sh
ENTRYPOINT [ "/project/scripts/init.sh" ]