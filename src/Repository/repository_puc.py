from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositoryPuc:
    """Repositorio CRUD y navegación para la tabla t_puc."""
    def __init__(self, conexion=None):
        self.conn = conexion or obtener_conexion()

    def insert(self, data: dict):
        cols = list(data.keys())
        vals = [data[c] for c in cols]
        placeholders = ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_puc ({', '.join(cols)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        assigns = ', '.join(f"{c} = %s" for c in data.keys())
        vals    = list(data.values())
        sql     = f"UPDATE t_puc SET {assigns} WHERE puc_cuenta = %s AND puc_cuent = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk[0], pk[1]])
            self.conn.commit()
        return True

    def delete(self, pk):
        sql = "DELETE FROM t_puc WHERE puc_cuenta = %s AND puc_cuent = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk[0], pk[1]))
            self.conn.commit()
        return True

    def first(self):
        sql = "SELECT * FROM t_puc ORDER BY puc_cuenta, puc_cuent ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        sql = (
            "SELECT * FROM t_puc "
            "WHERE (puc_cuenta, puc_cuent) < (%s, %s) "
            "ORDER BY puc_cuenta DESC, puc_cuent DESC LIMIT 1"
        )
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk[0], pk[1]))
            return cur.fetchone()

    def next(self, pk):
        sql = (
            "SELECT * FROM t_puc "
            "WHERE (puc_cuenta, puc_cuent) > (%s, %s) "
            "ORDER BY puc_cuenta ASC, puc_cuent ASC LIMIT 1"
        )
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk[0], pk[1]))
            return cur.fetchone()

    def last(self):
        sql = "SELECT * FROM t_puc ORDER BY puc_cuenta, puc_cuent DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        sql = "SELECT * FROM t_puc ORDER BY puc_cuenta, puc_cuent"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
