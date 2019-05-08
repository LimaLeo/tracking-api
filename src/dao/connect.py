from peewee import *
import os


db_name = os.environ['DB_NAME']
db_host = os.environ['DB_HOST']
db_port = os.environ['DB_PORT']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']

pg_db = PostgresqlDatabase(db_name,
                           user=db_user,
                           password=db_password,
                           host=db_host,
                           port=db_port
                           )
