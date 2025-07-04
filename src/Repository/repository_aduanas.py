from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositoryAduanas:
    """Repositorio para operaciones CRUD y navegación en la tabla t_aduana."""
    def __init__(self, conexion=None):
        # Usa la conexión externa o crea una nueva
        self.conn = conexion or obtener_conexion()
        self._crear_tabla_si_no_existe()

    def _crear_tabla_si_no_existe(self):
        """Crea la tabla t_aduana si no existe."""
        sql = """
        CREATE TABLE IF NOT EXISTS t_aduana (
            ad_codigo NUMERIC(2) PRIMARY KEY,
            ad_nombre VARCHAR(100)
        )
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
            self.conn.commit()

    def insert(self, data: dict):
        """Inserta un nuevo registro en t_aduana."""
        cols = list(data.keys())
        vals = [data[col] for col in cols]
        placeholders = ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_aduana ({', '.join(cols)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        """Actualiza un registro existente en t_aduana identificado por ad_codigo."""
        cols = [f"{col} = %s" for col in data.keys()]
        vals = list(data.values())
        sql = f"UPDATE t_aduana SET {', '.join(cols)} WHERE ad_codigo = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk])
            self.conn.commit()
        return True

    def delete(self, pk):
        """Elimina un registro de t_aduana identificado por ad_codigo."""
        sql = "DELETE FROM t_aduana WHERE ad_codigo = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            self.conn.commit()
        return True

    def first(self):
        """Obtiene el primer registro de t_aduana ordenado por ad_codigo asc."""
        sql = "SELECT * FROM t_aduana ORDER BY ad_codigo ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        """Obtiene el registro anterior al dado en t_aduana basado en ad_codigo."""
        sql = "SELECT * FROM t_aduana WHERE ad_codigo < %s ORDER BY ad_codigo DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def next(self, pk):
        """Obtiene el siguiente registro al dado en t_aduana basado en ad_codigo."""
        sql = "SELECT * FROM t_aduana WHERE ad_codigo > %s ORDER BY ad_codigo ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def last(self):
        """Obtiene el último registro de t_aduana ordenado por ad_codigo desc."""
        sql = "SELECT * FROM t_aduana ORDER BY ad_codigo DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        """Devuelve todos los registros de t_aduana ordenados por ad_codigo."""
        sql = "SELECT * FROM t_aduana ORDER BY ad_codigo"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()


def main():
    repo = RepositoryAduanas()

if __name__ == "__main__":
    main()
