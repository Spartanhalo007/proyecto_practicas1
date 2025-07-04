from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositorySegmen:
    """Repositorio CRUD y navegación para la tabla t_segmen."""
    def __init__(self, conexion=None):
        self.conn = conexion or obtener_conexion()

    def insert(self, data: dict):
        cols = list(data.keys())
        vals = [data[c] for c in cols]
        placeholders = ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_segmen ({', '.join(cols)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        assigns = ', '.join(f"{c} = %s" for c in data.keys())
        vals = list(data.values())
        sql = f"UPDATE t_segmen SET {assigns} WHERE segmen_cod = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk])
            self.conn.commit()
        return True

    def delete(self, pk):
        sql = "DELETE FROM t_segmen WHERE segmen_cod = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            self.conn.commit()
        return True

    def first(self):
        sql = "SELECT * FROM t_segmen ORDER BY segmen_cod ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        sql = "SELECT * FROM t_segmen WHERE segmen_cod < %s ORDER BY segmen_cod DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def next(self, pk):
        sql = "SELECT * FROM t_segmen WHERE segmen_cod > %s ORDER BY segmen_cod ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def last(self):
        sql = "SELECT * FROM t_segmen ORDER BY segmen_cod DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        sql = "SELECT * FROM t_segmen ORDER BY segmen_cod"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
