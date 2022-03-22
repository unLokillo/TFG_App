import sqlite3

conn = sqlite3.connect('./database.db')
c = conn.cursor()

user = "iii"


c.execute("""
    SELECT nickname, email, password 
            FROM Usuario
            WHERE nickname IS ?
                OR email IS ? 
""",(user,user))

pwd = c.fetchone()


"""
    INSERT INTO Usuario
    (
        id_user, nickname, name, surname, email, password, school, points, position, privileges
    ) VALUES (1, 'R', 'Rober', 'MR', 'rober@pescaneo.com', 'pass1234', 'ETSIINF', 0, 0, 'admin')
"""

#c.execute("DELETE FROM Usuario WHERE id_user IS 1")

conn.commit()
conn.close()