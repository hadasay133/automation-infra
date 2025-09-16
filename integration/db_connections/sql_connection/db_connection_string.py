from integration.db_connections.sql_connection.db_config import DBConfig


class DBConnection:
    def create_connection(self,db_config: DBConfig):
        match db_config.type:
            case "SQL Server":
                connection_string = (
                    f"mssql+pyodbc://@{db_config.server}/{db_config.database}"
                    f"?driver=ODBC+Driver+17+for+SQL+Server"
                    f"&trusted_connection=yes"
                )
                return connection_string
