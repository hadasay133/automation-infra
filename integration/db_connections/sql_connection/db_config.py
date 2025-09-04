import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

@dataclass
class DBConfig:
    # check other type of parameter
    #create factory for create  DBCONFIG

    def __init__(
        self,
        server: Optional[str] = None,
        database: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        type_of_db: Optional[str] = None, # create Enum
    ):
        config = {}
        config_path="C:\\Users\\USER\PycharmProjects\AutomationProgjectSeleniumSauseLabs\integration\db_details.json"
        if any(param is None for param in [server, database, username, password, type_of_db]):
            config = self._load_config(config_path)

        self.server = server if server is not None else config.get("server", "")
        self.database = database if database is not None else config.get("database", "")
        self.username = username if username is not None else config.get("username", "")
        self.password = password if password is not None else config.get("password", "")
        self.type = type_of_db if type_of_db is not None else config.get("type", "")

    def _load_config(self, config_path: str) -> Dict[str, str]:
        path = Path(config_path)
        if not path.exists():
            raise FileNotFoundError(f"Config file '{config_path}' not found.")
        with open(path, 'r') as f:
            return json.load(f)
