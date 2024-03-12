import sqlite3

conn = sqlite3.connect('EQUIPOS.DB')
cursor = conn.cursor()

try:
    cursor.execute('''CREATE TABLE Libertadores
                (id INTEGER PRIMARY KEY, Equipo TEXT, Jugador TEXT, posicion TEXT, edad INTEGER)''')
    conn.commit()
    print("Tabla de Libertadores creada correctamente.")
except sqlite3.Error as e:
    print("Error al crear la tabla:", e)

# Ejercicio 2: Insertar datos
Libertadores = [
    ('Nacional', 'dorlan pavon', 'MC', 37.0),
    ('Millonarios', 'Macalister silva', 'MC', 34.0),
    ('Flamengo', 'Arturo vidal', "MC", 36.0),
    ('Flamengo', 'Arturo vidal', "MC", 36.0),
    ('Boca junior', ' Sergio Romero', 'PO', 35.0),
    ('Raciong', 'Juan Quintero', 'MC', 32.0),
    ('Real Madrid', 'Vinicius JR', 'DC', 25.0),
    ('Real Madrid', 'Antonio Rudiger', 'DF', 30.0),
    ('Real Madrid', 'Dani Carvajal', 'DF', 32.0),
    ('Barcelona', 'Rober lewwandoski', 'DC', 35.0),
    ('Sao Paulo', 'James Rodriguez', 'MC', 32.0),
    ('Manchester United', 'Juan Ortiz', 'DF', 24.0),
    ('Fluminense', 'Marcelo Da Silva', 'DF', 24.0),
    ('Fluminense', 'German Cano', 'DF', 24)
]

try:
    cursor.executemany('INSERT INTO Libertadores (Equipo, Jugador, posicion, edad) VALUES (?, ?, ?, ?)', Libertadores)
    conn.commit()
    print("Datos insertados correctamente.")
except sqlite3.Error as e:
    print("Error al insertar datos:", e)

# Ejercicio 3: Consultar datos
try:
    cursor.execute('SELECT * FROM Libertadores WHERE edad > 30')
    resultado = cursor.fetchall()
    print("Jugadores que tengan una edad mayor a 30")
    for producto in resultado:
        print(producto)
except sqlite3.Error as e:
    print("Error al consultar datos:", e)

# Ejercicio 4: Actualizar datos
try:
    cursor.execute("UPDATE Libertadores SET posicion = 'MC'  WHERE edad = 30")
    conn.commit()
    print("Jugador actualiza posicion de DF a MC")
except sqlite3.Error as e:
    print("Error al actualizar datos:", e)

# Ejercicio 5: Eliminar datos
try:
    cursor.execute('DELETE FROM Libertadores WHERE id = 2')
    conn.commit()
    print("Jugador con id 2 eliminado de la base de datos.")
except sqlite3.Error as e:
    print("Error al eliminar datos:", e)

# Cerrar conexión
conn.close()