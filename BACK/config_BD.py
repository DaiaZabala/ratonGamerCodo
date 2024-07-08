import mysql.connector

try:
    conn = mysql.connector.connect(
        host='com24167.mysql.pythonanywhere-services.com',
        user='com24167',
        password='codo2024',
        database='com24167$default'
    )
    print("Conexión exitosa a MySQL en PythonAnywhere")
    conn.close()
except mysql.connector.Error as e:
    print(f"Error al conectar a MySQL: {e}")
