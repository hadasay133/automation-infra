from typing import Any
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
import logging

from integration.db_connections.sql_connection.db_config import DBConfig
from integration.db_connections.sql_connection.db_connection_string import DBConnection

# ToDo documentation
class SQLConnectionPoll:
    def __init__(self, db_config: DBConfig):
        db_connection=DBConnection()
        connection_string = db_connection.create_connection(db_config)
        self.engine: Engine = create_engine(
            connection_string,
            pool_size=10,
            max_overflow=5,
            pool_timeout=30,
            pool_recycle=180,
            future=True
        )
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )


    def  execute_non_select_query(self,query: str)-> bool:
            try:
                with self.engine.begin() as connection:
                    connection.execute(text(query))
                    return True
            except Exception as ex:
                print("Transaction failed:", ex)
                return False



    def execute_select_query(self,query: str)-> list[dict[str, Any]]:
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text(query))
                return [dict(row._mapping) for row in result.fetchall()]
        except SQLAlchemyError as e:
            self.logger.error(e, exc_info=True)

           # print(e)
            return []


    def select(self, query: str)->  list[dict[str, Any]] :
        return self.execute_select_query(query)

    def insert(self, query: str)-> bool:
        return self.execute_non_select_query(query)

    def update(self, query: str)-> bool:
        return self.execute_non_select_query(query)

    def delete(self, query: str)-> bool:
        return self.execute_non_select_query(query)



