from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositoryAutcom:
    """Repositorio para operaciones CRUD y navegación en la tabla t_autcom."""
    def __init__(self, conexion=None):
        self.conn = conexion or obtener_conexion()
        self._crear_tabla_si_no_existe()

    def _crear_tabla_si_no_existe(self):
        sql = """
        CREATE TABLE IF NOT EXISTS t_autcom (
            ac_nivel_c INTEGER PRIMARY KEY,
            ac_nombre VARCHAR(100),
            ac_descripcion TEXT
        )
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
            self.conn.commit()

    def insert(self, data: dict):
        cols = list(data.keys())
        vals = [data[col] for col in cols]
        placeholders = ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_autcom ({', '.join(cols)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        cols = [f"{col} = %s" for col in data.keys()]
        vals = list(data.values())
        sql = f"UPDATE t_autcom SET {', '.join(cols)} WHERE ac_nivel_c = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk])
            self.conn.commit()
        return True

    def delete(self, pk):
        sql = "DELETE FROM t_autcom WHERE ac_nivel_c = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            self.conn.commit()
        return True

    def first(self):
        sql = "SELECT * FROM t_autcom ORDER BY ac_nivel_c ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        sql = "SELECT * FROM t_autcom WHERE ac_nivel_c < %s ORDER BY ac_nivel_c DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def next(self, pk):
        sql = "SELECT * FROM t_autcom WHERE ac_nivel_c > %s ORDER BY ac_nivel_c ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def last(self):
        sql = "SELECT * FROM t_autcom ORDER BY ac_nivel_c DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        sql = "SELECT * FROM t_autcom ORDER BY ac_nivel_c"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()


def main():
    repo = RepositoryAutcom()
    print("Primero:", repo.first())
    print("Último:", repo.last())
    print("Todos:", repo.browse())

if __name__ == "__main__":
    main()
