from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositoryClient:
    """Repositorio CRUD y navegación para la tabla t_client."""
    def __init__(self, conexion=None):
        self.conn = conexion or obtener_conexion()
        self._crear_tabla_si_no_existe()

    def _crear_tabla_si_no_existe(self):
        sql = """
        CREATE TABLE IF NOT EXISTS t_client (
            cli_codigo INTEGER PRIMARY KEY,
            cli_nombre VARCHAR(100),
            cli_direccion VARCHAR(150),
            cli_telefono VARCHAR(30),
            cli_email VARCHAR(100)
        )
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
            self.conn.commit()

    def insert(self, data: dict):
        cols = list(data.keys())
        vals = [data[c] for c in cols]
        placeholders = ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_client ({', '.join(cols)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        assigns = ', '.join(f"{c} = %s" for c in data.keys())
        vals = list(data.values())
        sql = f"UPDATE t_client SET {assigns} WHERE cli_codigo = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk])
            self.conn.commit()
        return True

    def delete(self, pk):
        sql = "DELETE FROM t_client WHERE cli_codigo = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            self.conn.commit()
        return True

    def first(self):
        sql = "SELECT * FROM t_client ORDER BY cli_codigo ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        sql = "SELECT * FROM t_client WHERE cli_codigo < %s ORDER BY cli_codigo DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def next(self, pk):
        sql = "SELECT * FROM t_client WHERE cli_codigo > %s ORDER BY cli_codigo ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def last(self):
        sql = "SELECT * FROM t_client ORDER BY cli_codigo DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        sql = "SELECT * FROM t_client ORDER BY cli_codigo"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
