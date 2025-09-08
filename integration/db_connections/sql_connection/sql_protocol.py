from typing import Protocol, Tuple, Any, List, Optional, Dict


class SQLProtocol(Protocol):


    def insert(self, query: str) -> bool: ...

    def update(self, query: str) -> bool: ...

    def delete(self, query: str) -> bool: ...

    def select(self, query: str) -> list[dict[str, Any]] : ...

