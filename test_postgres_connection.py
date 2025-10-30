import psycopg2
from psycopg2 import OperationalError

def test_postgres_connection():
    try:
        conn = psycopg2.connect(
            dbname="intern_db",
            user="postgres",
            password="kesia",  
            host="localhost",
            port="5432"
        )
        print("PostgreSQL connection successful!")
        conn.close()
    except OperationalError as e:
        print("PostgreSQL connection failed:")
        print(e)

if __name__ == "__main__":
    test_postgres_connection()
