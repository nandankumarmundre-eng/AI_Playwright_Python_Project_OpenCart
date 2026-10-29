import sqlite3


def fetch_one(
    connection: sqlite3.Connection, query: str, parameters: tuple[object, ...] = ()
) -> sqlite3.Row | None:
    return connection.execute(query, parameters).fetchone()
