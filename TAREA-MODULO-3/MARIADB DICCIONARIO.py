import mysql.connector

# Conectar a la base de datos MariaDB
db = mysql.connector.connect(
    host='localhost',
    user='tu_usuario',
    password='tu_contraseña',
    database='tu_base_de_datos'
)
cursor = db.cursor()

def agregar_palabra():
    palabra = input("Introduce una palabra: ")
    significado = input("Introduce el significado de '{}': ".format(palabra))
    
    # Verificar si la palabra ya existe en la base de datos
    cursor.execute("SELECT * FROM diccionario WHERE palabra = %s", (palabra,))
    existe = cursor.fetchone()

    if existe:
        print("La palabra '{}' ya existe en el diccionario.".format(palabra))
    else:
        # Insertar nueva palabra en la base de datos
        cursor.execute("INSERT INTO diccionario (palabra, significado) VALUES (%s, %s)", (palabra, significado))
        db.commit()
        print("La palabra se agregó exitosamente al diccionario.")

def editar_palabra():
    palabra = input("Introduce una palabra para editar: ")
    nuevo_significado = input("Introduce el nuevo significado de '{}': ".format(palabra))

    # Verificar si la palabra existe en la base de datos
    cursor.execute("SELECT * FROM diccionario WHERE palabra = %s", (palabra,))
    existe = cursor.fetchone()

    if existe:
        # Actualizar el significado de la palabra en la base de datos
        cursor.execute("UPDATE diccionario SET significado = %s WHERE palabra = %s", (nuevo_significado, palabra))
        db.commit()
        print("Se actualizó el significado de '{}' exitosamente.".format(palabra))
    else:
        print("La palabra '{}' no está en el diccionario.".format(palabra))

def eliminar_palabra():
    palabra = input("Introduce una palabra para eliminar: ")

    # Verificar si la palabra existe en la base de datos
    cursor.execute("SELECT * FROM diccionario WHERE palabra = %s", (palabra,))
    existe = cursor.fetchone()

    if existe:
        # Eliminar la palabra de la base de datos
        cursor.execute("DELETE FROM diccionario WHERE palabra = %s", (palabra,))
        db.commit()
        print("Se eliminó la palabra '{}' del diccionario.".format(palabra))
    else:
        print("La palabra '{}' no está en el diccionario.".format(palabra))

def listar_palabras():
    # Obtener todas las palabras de la base de datos
    cursor.execute("SELECT palabra FROM diccionario")
    palabras = cursor.fetchall()

    if palabras:
        print("Lista de palabras en el diccionario:")
        for palabra in palabras:
            print(palabra[0])
    else:
        print("El diccionario está vacío.")

def buscar_significado():
    palabra = input("Introduce la palabra para buscar su significado: ")

    # Obtener el significado de la palabra desde la base de datos
    cursor.execute("SELECT significado FROM diccionario WHERE palabra = %s", (palabra,))
    significado = cursor.fetchone()

    if significado:
        print("El significado de '{}' es: {}".format(palabra, significado[0]))
    else:
        print("La palabra '{}' no está en el diccionario.".format(palabra))

def menu():
    print("\nBienvenido al diccionario.")
    print("Seleccione una opción:")
    print("a) Agregar nueva palabra")
    print("b) Editar palabra existente")
    print("c) Eliminar palabra existente")
    print("d) Ver listado de palabras")
    print("e) Buscar significado de palabra")
    print("f) Salir")

while True:
    menu()
    opcion = input("Ingrese su opción: ")
    if opcion == "a":
        agregar_palabra()
    elif opcion == "b":
        editar_palabra()
    elif opcion == "c":
        eliminar_palabra()
    elif opcion == "d":
        listar_palabras()
    elif opcion == "e":
        buscar_significado()
    elif opcion == "f":
        print("¡Hasta luego!")
        cursor.close()
        db.close()
        break
    else:
        print("Opción inválida.")
