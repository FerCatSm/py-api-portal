import os
import sqlalchemy
import datetime
import logging


def init_tcp_connection_engine(db_config):
    db_user = "postgres" #os.environ["DB_USER"]
    db_pass = "23people" #os.environ["DB_PASS"]
    db_name = "postgres" #os.environ["DB_NAME"]
    db_host = "34.70.74.170:5432" #os.environ["DB_HOST"]

    # Extract host and port from db_host
    host_args = db_host.split(":")
    db_hostname, db_port = host_args[0], int(host_args[1])

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="postgres+pg8000",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            host=db_hostname,  # e.g. "127.0.0.1"
            port=db_port,  # e.g. 5432
            database=db_name  # e.g. "my-database-name"
        ),
        **db_config

    )

    return pool
