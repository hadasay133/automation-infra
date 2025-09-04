from typing import   Tuple, List

import pyodbc
from integration.db_connections.sql_connection.db_config import DBConfig


class SQLServiceb:

    def __init__(self,db_config:DBConfig):
        pyodbc.pooling = True
        self.db_config = db_config
        self.connection = None
        self.cursor = None

    def _connect(self):
        try:
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.db_config.server};DATABASE={self.db_config.database };'
            if self.db_config.password:
                conn_str += f'UID={self.db_config.username};PWD={self.db_config.password}'
            else:
                # אם אין סיסמא, אפשר להשתמש בהתחברות Windows Authentication
                conn_str += f'Trusted_Connection=yes;'

            # יצירת החיבור
            self.connection = pyodbc.connect(conn_str)
            self.cursor = self.connection.cursor()
            print("Database connection successful")
        except Exception as e:
            print(f"Error connecting to DB: {e}")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            if query.strip().lower().startswith("select"):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return None
        except Exception as e:
            print(f"Error executing query: {e}")
            self.close()
            return []

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def insert(self, query: str):
        self._connect()
        self.execute_query(query)
        self.close()

    def update(self, query: str):
        self._connect()
        self.execute_query(query)
        self.close()

    def delete(self, query: str):
        self._connect()
        self.execute_query(query)
        self.close()



    def select(self, query: str) -> List[Tuple]:
        self._connect()
        result:List[Tuple] = self.execute_query(query)
        self.connection.close()
        return result


