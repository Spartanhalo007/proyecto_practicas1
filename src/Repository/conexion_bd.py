import psycopg2

config = {
    "dbname"    : "TablasyParametros",
    "user"      : "postgres",
    "password"  : "DB",
    "host"      : "localhost",
    "port"      : "5432"
}

def obtener_conexion():

    try:
        conn = psycopg2.connect(**config)
        print("✅ Conectado exitosamente con JSON")
        return conn
    except Exception as e:
        print("❌ Error:", e)
        return None

