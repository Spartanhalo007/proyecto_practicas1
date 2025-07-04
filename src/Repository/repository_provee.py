from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositoryProvee:
    """Repositorio CRUD y navegación para la tabla t_provee."""
    def __init__(self, conexion=None):
        self.conn = conexion or obtener_conexion()

    def insert(self, data: dict):
        cols        = list(data.keys())
        vals        = [data[c] for c in cols]
        placeholders= ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_provee ({', '.join(cols)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        assigns = ', '.join(f"{c} = %s" for c in data.keys())
        vals    = list(data.values())
        sql     = f"UPDATE t_provee SET {assigns} WHERE pr_tp = %s AND pr_codigo = %s"
        # Usamos combinación de PR_TP y PR_CODIGO como clave compuesta
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk[0], pk[1]])
            self.conn.commit()
        return True

    def delete(self, pk):
        sql = "DELETE FROM t_provee WHERE pr_tp = %s AND pr_codigo = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk[0], pk[1]))
            self.conn.commit()
        return True

    def first(self):
        sql = "SELECT * FROM t_provee ORDER BY pr_tp, pr_codigo ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        sql = ("SELECT * FROM t_provee "
               "WHERE (pr_tp, pr_codigo) < (%s, %s) "
               "ORDER BY pr_tp DESC, pr_codigo DESC LIMIT 1")
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk[0], pk[1]))
            return cur.fetchone()

    def next(self, pk):
        sql = ("SELECT * FROM t_provee "
               "WHERE (pr_tp, pr_codigo) > (%s, %s) "
               "ORDER BY pr_tp ASC, pr_codigo ASC LIMIT 1")
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk[0], pk[1]))
            return cur.fetchone()

    def last(self):
        sql = "SELECT * FROM t_provee ORDER BY pr_tp, pr_codigo DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        sql = "SELECT * FROM t_provee ORDER BY pr_tp, pr_codigo"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
