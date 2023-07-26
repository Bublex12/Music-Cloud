import os
import psycopg2
from psycopg2 import extensions


def get_connection() -> extensions.connection:
    return psycopg2.connect(
        database=os.getenv("DB"),
        user=os.getenv("USER_DB"),
        password=os.getenv("PASS_DB"),
        host=os.getenv("HOST_DB"),
        port=os.getenv("PORT_DB")
    )


def get_connection_test() -> extensions.connection:
    return psycopg2.connect(

            database="gigaBi",
            user="postgres",
            password="a2414119678",
            host="localhost",
            port="5432"
)