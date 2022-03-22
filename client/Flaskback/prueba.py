import sqlite3

def checklogin (jsonob):
    conn = sqlite3.connect("C:/Users/rober/'OneDrive - Universidad Politécnica de Madrid'/'4º Ingeniería Informática'/'2º semestre'/'Trabajo de final de grado'/'TFG code'/client/db/database1.db")
    c = conn.cursor()
    print("Conexión completada\n")

    username = jsonob
    c.execute("""
        SELECT nickname, email, password 
        FROM Usuario
        WHERE nickname IS ?
            OR email IS ? 
    """,(username, username))
    usuario = c.fetchone()
    conn
    return (usuario)
"""
c.execute("SELECT * FROM Usuario")
users = c.fetchall()
print(users)
conn.close()
"""