# Core Library
import os
from os.path import dirname, join
from pathlib import Path

# Third party
import mysql.connector
from dotenv import load_dotenv

dotenv_path = Path(__file__).parent.parent / ".env.local"
load_dotenv(dotenv_path)

config = {
    "user": os.getenv("USER_DB"),
    "password": os.getenv("PASS_DB"),
    "host": os.getenv("HOST_DB"),
    "port": os.getenv("PORT_DB"),
    "database": os.getenv("DATABASE_DB"),
    "raise_on_warnings": True,
}


def with_connection(f):
    def with_connection_(*args, **kwargs):
        conn = mysql.connector.Connect(**config)
        try:
            result = f(*args, connection=conn, **kwargs)
        except mysql.connector.Error as e:
            conn.rollback()
            print(f"Error SQL: {str(e)}")
            raise
        else:
            conn.commit()
        finally:
            conn.close()
        return result

    return with_connection_
