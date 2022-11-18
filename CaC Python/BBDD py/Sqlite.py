'''Python y BBDD
Python es capaz de manipular datos dentro de un BD
Pasos a seguir para conectar con un BD
    1. Abrir/Crear conexión
    2 Crear puntero: objeto que nos permite ejecutar un query y manejar el resultado
    3. Ejecutar query
    4. Manejar los resultados de la query (consulta) -> insertar, leer, actualizar, borrar
    5. Cerrar puntero
    6. Cerrar la conexión
'''

from asyncio.windows_events import NULL
import sqlite3 as sq3

# crear una conexión a la BBDD
con = sq3.connect('mi_db.db') # "mi_db.db" es el nombre de la base de datos. Se crea la conexión a la Base de Datos y se asigna a la variable "con"

# Creamos Puntero o cursor
cur = con.cursor()
# Es el encargado de la comunicación con la Base de Datos

# CREAR TABLE
# Formato String
# _id agrega el autoincrement
instruct1 = '''CREATE TABLE IF NOT EXISTS escuelas(
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(45) DEFAULT NULL,
    localidad varchar(45) DEFAULT NULL,
    provincia varchar(45) DEFAULT NULL,
    capacidad INTEGER DEFAULT NULL)'''

instruct2 = '''CREATE TABLE IF NOT EXISTS alumnos(
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_escuela INTEGER DEFAULT NULL,
    legajo INTEGER DEFAULT NULL,
    nombre varchar(45) DEFAULT NULL,
    nota decimal(10,0) DEFAULT NULL,
    grado INTEGER DEFAULT NULL,
    email varchar(45) NOT NULL,
    FOREIGN KEY (id_escuela) REFERENCES escuelas(id))'''

# Execute() Método para ejecutar comandos SQL. Ejecuta una sola instrucción SQL.
cur.execute(instruct1)
cur.execute(instruct2)

lista1 = [(1,'Normal 1','Quilmes','Buenos Aires',250),(2,'Gral. San Martín','San Salvador','Jujuy',100),(3,'Belgrano','Belgrano','Córdoba',150),(4,'EET Nro 2','Avellaneda','Buenos Aires',500),(5,'Esc. N° 2 Tomás Santa coloma','Capital Federal','Buenos Aires',250)]
lista2 = [(1,2,1000,'Ramón Mesa',8,1,'rmesa@mail.com'),(2,2,1002,'Tomás Smith',8,1,''),(4,1,101,'Juan Perez',10,3,''),(5,1,105,'Pedro González',9,3,''),(6,5,190,'Roberto Luis Sánchez',8,3,'robertoluissanchez@gmail.com'),(7,2,106,'Martín Bossio',NULL,3,''),(8,4,100,'Paula Remmi',3,1,'mail@mail.com'),(9,4,1234,'Pedro Gómez',6,2,'')]


# INSERTAR DATA
cur.executemany('INSERT OR IGNORE INTO escuelas VALUES (?,?,?,?,?)', lista1) # argumentos
cur.executemany('INSERT OR IGNORE INTO alumnos VALUES (?,?,?,?,?,?,?)', lista2) # argumentos

# Consulta BBDD en formato String
query1 = '''SELECT alumnos.legajo, alumnos.nombre, alumnos.nota, alumnos.email,
escuelas.nombre, escuelas.localidad, escuelas.provincia FROM alumnos
INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id''' 

cur.execute(query1)

mostrar = cur.fetchall() # Obtiene todas las filas del resultado de una consulta y devuelve lista
print(mostrar)

print()

# Muestra elementos (tuplas) de la lista
for registro in cur.execute(query1):
    print(registro)

print()

for registro in cur.execute(query1):
    print("     Legajo : ", registro[0])
    print("     Nombre : ", registro[1])
    print("     Nota : ", registro[2])
    print("     Email : ", registro[3])
    print("     Escuela : ", registro[4])
    print("     Localidad: ", registro[5])
    print("     Provincia : ", registro[6])
    print()

con.commit() # submite la transacción actual, los efectos de un declaración SQL, a la Base de datos
con.close() # Termina la conexión con la Base de datos al final del código de programación
