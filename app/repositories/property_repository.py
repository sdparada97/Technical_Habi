# Core Library
from dataclasses import dataclass
from typing import List

# First party
from app.db import with_connection
from app.repositories.base_repository import IRepository


@dataclass
class Join:
    table: str
    condition: str


class PropertyRepository(IRepository):
    @with_connection
    def get_all_with_filters(self, fields, joins: List[Join], params, **kwargs):
        conn = kwargs.pop("connection")
        cur = conn.cursor(buffered=True, dictionary=True)

        query = f"""
                SELECT {",".join(fields)}
                FROM property p
                {" ".join(map(lambda join: f"INNER JOIN {join.table} ON {join.condition}", joins))}
                WHERE {params}
                """
        cur.execute(query)

        return cur.fetchall()

    @with_connection
    def get_all(self, **kwargs):
        pass

    @with_connection
    def get_by_id(self, id, **kwargs):
        pass

    @with_connection
    def create(self, property, **kwargs):
        pass

    @with_connection
    def update(self, property, **kwargs):
        pass

    @with_connection
    def delete(self, id, **kwargs):
        pass
