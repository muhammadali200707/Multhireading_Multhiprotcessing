import os
import psycopg2
import psycopg2 as psql
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str) -> str or list:
        db = psql.connect(
            database=os.getenv('db_name'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            host=os.getenv('db_host'),
            port=os.getenv('db_port'),
        )
        cursor = db.cursor()
        cursor.execute(query)
        data = ['insert', 'delete', 'update', 'alter']
        if query_type in data:
            db.commit()
            if query_type == 'insert':
                return 'inserted successfully'
            elif query_type == 'delete':
                return 'deleted successfully'
            elif query_type == 'update':
                return 'updated successfully'
            elif query_type == 'alter':
                return 'altered successfully'
            else:
                return 'selected successfully'

        return cursor.fetchall()

