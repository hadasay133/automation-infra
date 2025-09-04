from typing import Any

from integration.db_connections.sql_connection.db_config import DBConfig
from integration.db_connections.sql_connection.sql_protocol import SQLProtocol
from integration.db_connections.sql_connection.db_pool import  SQLConnectionPoll


class SQLService(SQLProtocol):

    def __init__(self,db_config:DBConfig):
        self.db_config = db_config
        self.sql_connection= SQLConnectionPoll(db_config)


    def insert(self, query: str):
         self.sql_connection.insert(query)

    def update(self, query: str)-> bool:
        return self.sql_connection.update(query)

    def select(self, query: str) ->  list[dict[str, Any]]:
        return self.sql_connection.select(query)

    def delete(self,query: str)-> bool:
        return self.sql_connection.delete(query)