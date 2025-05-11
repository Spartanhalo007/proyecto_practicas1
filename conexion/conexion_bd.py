import psycopg2

def obtener_conexion():
    try: 
        conexion = psycopg2.connect(
            host="localhost",
            database="TablasyParametros",
            user="postgres",
            password="BD"
        )
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None
