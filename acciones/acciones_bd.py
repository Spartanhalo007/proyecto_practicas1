import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexion.conexion_bd import obtener_conexion

def guardar_aduana(codigo, nombre):
    conexion = obtener_conexion()
    if conexion is None:
        print("No hay conexión con la base de datos.")
        return False

    try:
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO t_aduana (ad_codigo, ad_nombre) VALUES (%s, %s)",
                    (codigo, nombre)
                )
        print("Registro guardado correctamente.")
        return True
    except Exception as e:
        print("Error al guardar datos:", e)
        return False
    finally:
        conexion.close()

def eliminar_aduana(codigo):
    conexion = obtener_conexion()

    if conexion is None:
        print("No hay conexión con la base de datos.")
        return False
    
    try:
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM t_aduana WHERE ad_codigo = %s",
                    (codigo,)
                )
                if cursor.rowcount == 0:
                    print("No se encontro nunguin registro con ese codigo")
                    return False
        print("registro eliminado correctamente.")
        return True
    except Exception as e:
        print("Error al eliminar datos.", e)
        return False
    finally:
        conexion.close()

def consultar_aduana(codigo):
    conexion = obtener_conexion()

    if conexion is None:
        print("No hay conexión con la base de datos.")
        return False
    
    try: 
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM t_aduana WHERE ad_codigo = %s", 
                           (codigo,))
            resultado = cursor.fetchone()
            return resultado
    except Exception as e:
        print(f"Error al consultar: {e}")
        return None
    finally:
        conexion.close()

    