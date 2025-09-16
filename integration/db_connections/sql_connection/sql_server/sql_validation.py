import re
from typing import Dict, Tuple, Any, List


class SqlValidation:
    def __init__(self, allowed_tables: set, allowed_columns: Dict[str, set]):
        self.allowed_tables = allowed_tables
        self.allowed_columns = allowed_columns

    def validate_table(self, table_name: str) -> bool:
        if table_name not in self.allowed_tables:
            print(f"Table '{table_name}' is not allowed")
            return False
        return True
    def validate_columns(self, table_name: str, columns: List[str]) -> bool:
        if table_name not in self.allowed_columns:
            print(f"No columns defined for table '{table_name}'")
            return False
        invalid = set(columns) - self.allowed_columns[table_name]
        if invalid:
            print(f"Invalid columns for table '{table_name}': {invalid}")
            return False
        return True
    def build_insert_query (self, table: str, columns: Dict[str, Any]) -> Tuple[str, Tuple[Any, ...]]:
        column_names = ', '.join(columns.keys())
        placeholders = ', '.join(['?'] * len(columns))
        values = tuple(columns.values())
        query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
        return query, values

    def build_update_query(self, table: str,
                           set_clause: Dict[str, Any],
                           where_clause: str,
                           where_params: Tuple[Any, ...])-> Tuple[str, Tuple[Any, ...]]:
        set_str = ', '.join([f"{col} = ?" for col in set_clause.keys()])
        values = tuple(set_clause.values())
        query = f"UPDATE {table} SET {set_str} WHERE {where_clause}"
        return query, values+where_params

    def build_delete_query(self, table: str,
                           where_clause : Dict[str, Any],
                           where_params: Tuple[Any, ...])->Tuple[str, Tuple[Any, ...]]:
        query = f"DELETE FROM {table} where {where_clause} "
        return query, where_params

    def check_select_query(self, query: str) -> bool:
        lowered = query.strip().lower()
        # מרשה רק SELECT, לא DELETE/INSERT שמתחבאים בפנים
        return lowered.startswith("select") and "drop" not in lowered and ";" not in lowered[6:]

    def is_safe_identifier(self,name):
        return re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name) is not None