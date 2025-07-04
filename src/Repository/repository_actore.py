from Repository.repository import *
from Repository.conexion_bd import obtener_conexion

class RepositoryActore:
    """Repositorio para operaciones CRUD y navegación en la tabla t_actore."""
    def __init__(self, conexion=None):
        self.conn = conexion or obtener_conexion()
        self._crear_tabla_si_no_existe()

    def _crear_tabla_si_no_existe(self):
        """Crea la tabla t_actore si no existe."""
        sql = """
        CREATE TABLE IF NOT EXISTS t_actore (
            ac_f_cremo   VARCHAR(10),
            ac_tip_act   NUMERIC(1),
            ac_tip_con   VARCHAR(45),
            ac_tp_idvc   VARCHAR(2),
            ac_tp_id     VARCHAR(3),
            ac_nu_id     VARCHAR(20) PRIMARY KEY,
            ac_nombre    VARCHAR(100),
            ac_ciudad    VARCHAR(5),
            ac_nom_ciu   VARCHAR(45),
            ac_ciiu      VARCHAR(4),
            ac_ciiunom   VARCHAR(50),
            ac_telef     VARCHAR(25),
            ac_direcc    VARCHAR(100),
            ac_correo    VARCHAR(100),
            ac_tp_empr   NUMERIC(4),
            ac_tp_emno   VARCHAR(60),
            ac_sector    VARCHAR(2),
            ac_sec_nom   VARCHAR(10),
            ac_tp_efin   NUMERIC(3),
            ac_tiefino   VARCHAR(45),
            ac_supervi   NUMERIC(3),
            ac_tp_sinp   VARCHAR(3),
            ac_tp_sino   VARCHAR(30),
            ac_regimen   NUMERIC(3),
            ac_regi_no   VARCHAR(10),
            ac_act_sue   NUMERIC(1),
            ac_nu_admi   NUMERIC(15),
            ac_nu_patr   NUMERIC(15),
            ac_no_patr   VARCHAR(100),
            ac_tpidvac   VARCHAR(2),
            ac_natural   NUMERIC(3),
            ac_paisres   VARCHAR(3)
        )
        """
        with self.conn.cursor() as cur:
            cur.execute(sql)
            self.conn.commit()

    def insert(self, data: dict):
        cols = list(data.keys())
        vals = [data[col] for col in cols]
        placeholders = ', '.join(['%s'] * len(cols))
        sql = f"INSERT INTO t_actore ({', '.join(cols)}) VALUES ({placeholders})"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals)
            self.conn.commit()
        return True

    def update(self, pk, data: dict):
        cols = [f"{col} = %s" for col in data.keys()]
        vals = list(data.values())
        sql = f"UPDATE t_actore SET {', '.join(cols)} WHERE ac_nu_id = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, vals + [pk])
            self.conn.commit()
        return True

    def delete(self, pk):
        sql = "DELETE FROM t_actore WHERE ac_nu_id = %s"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            self.conn.commit()
        return True

    def first(self):
        sql = "SELECT * FROM t_actore ORDER BY ac_nu_id ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def prev(self, pk):
        sql = "SELECT * FROM t_actore WHERE ac_nu_id < %s ORDER BY ac_nu_id DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def next(self, pk):
        sql = "SELECT * FROM t_actore WHERE ac_nu_id > %s ORDER BY ac_nu_id ASC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql, (pk,))
            return cur.fetchone()

    def last(self):
        sql = "SELECT * FROM t_actore ORDER BY ac_nu_id DESC LIMIT 1"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def browse(self):
        sql = "SELECT * FROM t_actore ORDER BY ac_nu_id"
        with self.conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
