from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositoryCam053:
    """CRUD y navegación para t_cam053."""
    def __init__(self, conexion=None):
        self.conn = conexion or obtener_conexion()

    def insert(self, data: dict):
        cols = list(data.keys())
        vals = [data[c] for c in cols]
        ph = ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_cam053 ({', '.join(cols)}) VALUES ({ph})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        assigns = ', '.join(f"{c} = %s" for c in data.keys())
        vals = list(data.values())
        sql = f"UPDATE t_cam053 SET {assigns} WHERE pc8_conse = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk])
            self.conn.commit()
        return True

    def delete(self, pk):
        sql = "DELETE FROM t_cam053 WHERE pc8_conse = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            self.conn.commit()
        return True

    def first(self):
        sql = "SELECT * FROM t_cam053 ORDER BY pc8_conse ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        sql = "SELECT * FROM t_cam053 WHERE pc8_conse < %s ORDER BY pc8_conse DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def next(self, pk):
        sql = "SELECT * FROM t_cam053 WHERE pc8_conse > %s ORDER BY pc8_conse ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def last(self):
        sql = "SELECT * FROM t_cam053 ORDER BY pc8_conse DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        sql = "SELECT * FROM t_cam053 ORDER BY pc8_conse"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
