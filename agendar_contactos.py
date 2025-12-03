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
        print("No hay resultados todavía")

def editar_contacto(id_contacto, nuevo_telefono, nuevo_nombre):
    connect = sqlite3.connect('agenda.db')
    cursor = connect.cursor()
    cursor.execute("UPDATE contactos SET nombre = ?, telefono = ? WHERE id_contacto = ?", (nuevo_nombre, nuevo_telefono, id_contacto))
    connect.commit()

    if cursor.rowcount > 0:
        print("Se editó correctamente el contacto...")
    else:
        print("No existe ese contacto...")
    connect.close()

def eliminar_contacto(id_contacto):
    connect = sqlite3.connect('agenda.db')
    cursor = connect.cursor()
    cursor.execute("DELETE FROM contactos WHERE id_contacto = ?", (id_contacto,))
    connect.commit()

    if cursor.rowcount > 0:
        print("Se eliminó correctamente el contacto...")
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
        print("\n Bienvenido al menú crack, ¿qué deseas hacer?")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Ver todos")
        print("6. Salir")

        try:
            opcion = int(input("Escoge la opción: "))
        except ValueError:
            print("Escoge solo números, nada de letras :)")
            continue
        
        if opcion == 1:
            
            nombre = input("Nombre: ").strip()

            
            if any(char.isdigit() for char in nombre) or nombre == "":
                print("Solo letras y no puede estar vacío")
                continue  

            
            while True:
                telefono = input("Telefono: ").strip()
                if telefono.isdigit() and telefono != "":
                    break
                else:
                    print("El teléfono solo debe contener números y no puede estar vacío")

           
            agregar(nombre, telefono)

        elif opcion == 2:
            
            while True:
                nombre = input("Buscar nombre: ").strip()
                if any(char.isdigit() for char in nombre) or nombre == "":
                    print("Solo escribe letras y no puede estar vacío.")
                else:
                    buscar_contacto(nombre)
                    break

        elif opcion == 3:
            
            try:
                id_contacto = int(input("Id del contacto a editar: "))
            except ValueError:
                print("Solo números para el ID")
                continue

            nuevo_nombre = input("Nuevo nombre: ").strip()
            if any(char.isdigit() for char in nuevo_nombre) or nuevo_nombre == "":
                print("Solo letras y no puede estar vacío")
                continue

            while True:
                nuevo_telefono = input("Nuevo teléfono: ").strip()
                if nuevo_telefono.isdigit() and nuevo_telefono != "":
                    break
                else:
                    print(" El teléfono solo debe contener números y no puede estar vacío")

            editar_contacto(id_contacto, nuevo_telefono, nuevo_nombre)

        elif opcion == 4:
            
            try:
                id_contacto = int(input("Selecciona ID del contacto a eliminar: "))
                eliminar_contacto(id_contacto)
            except ValueError:
                print(" Solo pon el ID (número), nada de letras")

        elif opcion == 5:
            mostrar_todo()

        elif opcion == 6:
            print("Saliendo...")
            break

        else:
            print(" Opción incorrecta, vuelve a intentar")

crear_db()
menu()
