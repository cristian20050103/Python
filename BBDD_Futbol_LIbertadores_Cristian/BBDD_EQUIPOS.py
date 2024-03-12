import sqlite3

# Establecer una conexión con la base de datos SQLite llamada 'EQUIPOS.DB'
conn = sqlite3.connect('EQUIPOS.DB')
cursor = conn.cursor()

try:
    # Crear una tabla llamada 'Libertadores' con columnas específicas
    cursor.execute('''CREATE TABLE Libertadores
                (id INTEGER PRIMARY KEY, Equipo TEXT, Jugador TEXT, posicion TEXT, edad INTEGER)''')
    conn.commit()
    print("Tabla de Libertadores creada correctamente.")
except sqlite3.Error as e:
    print("Error al crear la tabla:", e)

# Ejercicio 2: Insertar datos
Libertadores = [
    ('Nacional', 'Dorlan Pavón', 'MC', 37),
    ('Millonarios', 'Macalister Silva', 'MC', 34),
    ('Flamengo', 'Arturo Vidal', 'MC', 36),
    ('Flamengo', 'Arturo Vidal', 'MC', 36),
    ('Boca Juniors', 'Sergio Romero', 'PO', 35),
    ('Racing', 'Juan Quintero', 'MC', 32),
    ('Real Madrid', 'Vinicius Jr.', 'DC', 25),
    ('Real Madrid', 'Antonio Rudiger', 'DF', 30),
    ('Real Madrid', 'Dani Carvajal', 'DF', 32),
    ('Barcelona', 'Robert Lewandowski', 'DC', 35),
    ('Sao Paulo', 'James Rodriguez', 'MC', 32),
    ('Manchester United', 'Juan Ortiz', 'DF', 24),
    ('Fluminense', 'Marcelo Da Silva', 'DF', 24),
    ('Fluminense', 'German Cano', 'DF', 24),
    ('Al-Nassrr', 'Cristiano Ronaldo', 'DC', 24)
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
    print("Jugador actualiza posición de DF a MC")
except sqlite3.Error as e:
    print("Error al actualizar datos:", e)

# Ejercicio 5: Eliminar datos
try:
    cursor.execute('DELETE FROM Libertadores WHERE id = 2')
    conn.commit()
    print("Jugador con id 2 eliminado de la base de datos.")
except sqlite3.Error as e:
    print("Error al eliminar datos:", e)

conn.close()
