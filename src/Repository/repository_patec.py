from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositoryPatec:
    """Repositorio CRUD y navegación para la tabla t_patec."""
    def __init__(self, conexion=None):
        self.conn = conexion or obtener_conexion()

    def insert(self, data: dict):
        cols        = list(data.keys())
        vals        = [data[c] for c in cols]
        placeholders= ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_patec ({', '.join(cols)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        assigns = ', '.join(f"{c} = %s" for c in data.keys())
        vals    = list(data.values())
        sql     = f"UPDATE t_patec SET {assigns} WHERE pt_fecha = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk])
            self.conn.commit()
        return True

    def delete(self, pk):
        sql = "DELETE FROM t_patec WHERE pt_fecha = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            self.conn.commit()
        return True

    def first(self):
        sql = "SELECT * FROM t_patec ORDER BY pt_fecha ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        sql = "SELECT * FROM t_patec WHERE pt_fecha < %s ORDER BY pt_fecha DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def next(self, pk):
        sql = "SELECT * FROM t_patec WHERE pt_fecha > %s ORDER BY pt_fecha ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def last(self):
        sql = "SELECT * FROM t_patec ORDER BY pt_fecha DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        sql = "SELECT * FROM t_patec ORDER BY pt_fecha"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
