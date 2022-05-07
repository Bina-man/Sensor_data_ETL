import os
import glob


def get_sql_files(src_path):
  
  return glob.glob(f'{src_path}*.sql')


def convert_sql(sql_satement, target_path, file_name):
  # ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci
  # `
  # sql
  postgres_sql = sql_satement.lower()
  postgres_sql = postgres_sql.replace(";", "")
  postgres_sql = postgres_sql.strip()

  postgres_sql = postgres_sql.replace("ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci".lower(), "")
  postgres_sql = postgres_sql.replace("ENGINE=InnoDB DEFAULT CHARSET=utf8".lower(), "")
  postgres_sql = postgres_sql.replace("double".lower(), "double precision")

  postgres_sql = postgres_sql.replace("`", "")
  postgres_sql = postgres_sql.strip() + ";"


  if postgres_sql.split()[0] == 'load':
    # to do load handler
    pass
  if postgres_sql.split()[0] == 'create':
     with open(f'{target_path}/{file_name}', 'w', encoding = 'utf-8') as _file:
      _file.write(postgres_sql)

def convert_create_statements(src_path="/airflow/dags/mysqlSql/", tgt_path="/airflow/dags/postgresSql/"):
  sql_files = get_sql_files(src_path)
  for sql_file in sql_files:
    file_name = sql_file.split("/")[-1]
    with open(sql_file, encoding = 'utf-8') as _file:
      convert_sql(_file.read(), tgt_path, file_name=file_name)
    
    

  




