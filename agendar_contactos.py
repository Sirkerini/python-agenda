import sqlite3

def crear_db():
 connect = sqlite3.connect('agenda.db')
 cursor = connect.cursor()
 cursor.execute("""
    CREATE TABLE IF NOT EXISTS contactos(
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT NOT NULL
    )
""")
 connect.commit()
 connect.close()

def agregar(nombre, telefono):
 connect = sqlite3.connect('agenda.db')
 cursor = connect.cursor()
 cursor.execute("INSERT INTO contactos (nombre, telefono) VALUES (?,?)", (nombre, telefono))
 connect.commit()
 connect.close()
 print("Contacto agregado correctamente...")


def buscar_contacto(nombre):
 connect = sqlite3.connect('agenda.db')
 cursor = connect.cursor()
 cursor.execute("SELECT nombre, telefono FROM contactos WHERE nombre LIKE ?", ('%' + nombre + '%',))
 resultados = cursor.fetchall()
 connect.close()

 if resultados:
  print("\n Resultados de contactos:")
  for r in resultados:
   print(f"{r[0]} : {r[1]}")
 else:
  print("No hay resultados todavia")


def editar_contacto(id_contacto, nuevo_telefono, nuevo_nombre):
 connect = sqlite3.connect('agenda.db')
 cursor = connect.cursor()
 cursor.execute("UPDATE contactos SET nombre = ?, telefono = ? WHERE id_contacto = ?", (nuevo_nombre, nuevo_telefono, id_contacto))
 connect.commit()

 if cursor.rowcount > 0:
  print("Se edito bien el contacto...")

 else:
  print("No existe ese contacto...")
 connect.close()


def eliminar_contacto(id_contacto):
 connect = sqlite3.connect('agenda.db')
 cursor = connect.cursor()
 cursor.execute("DELETE FROM contactos WHERE id_contacto = ?", (id_contacto,))
 connect.commit()

 if cursor.rowcount > 0:
  print("Se elimino bien el contacto...")

 else:
  print("No existe ese contacto...")
 connect.close()

def mostrar_todo():
 connect = sqlite3.connect('agenda.db')
 cursor = connect.cursor()
 cursor.execute("SELECT id_contacto, nombre, telefono FROM contactos ORDER BY nombre")
 contactos = cursor.fetchall()
 connect.close()

 if contactos:
   print("\n Lista de contactos:")
   for c in contactos:
    print(f"{c[0]} - {c[1]}: {c[2]}")
 else:
  print("No hay contactos")


def menu():
    while True:
     print("\n Bienvenido al menu crack, que deseas hacer: ")
     print("1. Agregar contacto")
     print("2. Buscar contacto")
     print("3. Editar contacto")
     print("4. Eliminar contacto")
     print("5. Ver todos")
     print("6. Salir")
     opcion = int(input("Escoge la opcion: "))


     if opcion == 1:
      nombre = input("Nombre: ")
      telefono = input("Telefono: ")
      agregar(nombre, telefono)

     elif opcion == 2:
      nombre = input("Buscar nombre: ")
      buscar_contacto(nombre)

     elif opcion == 3:
      print("El id es requerido para cambiar el nombre de contacto ")
      id_contacto = int(input("Id: "))
      nuevo_nombre = input("Nombre: ")
      nuevo_telefono = input("Telefono: ")
      editar_contacto(id_contacto, nuevo_telefono, nuevo_nombre)

     elif opcion == 4:
      id_contacto = int(input("Selecciona id: "))
      eliminar_contacto(id_contacto)

     elif opcion == 5:
      mostrar_todo()

     elif opcion == 6:
      print("Saliendo...")
      break
     else:
      print("Es incorrecta la opcion, vuelve a intentar")

crear_db()
menu()