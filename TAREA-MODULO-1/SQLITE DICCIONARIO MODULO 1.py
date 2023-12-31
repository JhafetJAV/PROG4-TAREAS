import sqlite3
import os

APP_PATH = os.getcwd()
DB_PATH = APP_PATH +'/w11.db'

con = sqlite3.connect(DB_PATH)
cursor = con.cursor()
try:
   def crear_tabla():
    cursor.execute("""
            CREATE TABLE  diccionario(
            ID            INTEGER         PRIMARY KEY     AUTOINCREMENT,
            PALABRA        TEXT                           NOT NULL,
            SIGNIFICADO    TEXT                           NOT NULL
            )
            """
)
except Exception as e:
    print (e)

try:
 def agregar_palabra(palabra,significado):
    sentencia = "INSERT INTO diccionario(palabra, significado) VALUES (?,?)"
    cursor.execute (sentencia,[palabra,significado])
    con.commit()

 def editar_palabra(palabra, nuevosignificado):
    sentencia = "UPDATE diccionario SET significado = ? WHERE palabra = ?"
    cursor.execute (sentencia,[nuevosignificado, palabra])
    con.commit()

 def Eliminarpalabra(palabra):
    sentencia = "DELETE FROM diccionario WHERE palabra = ?"
    cursor.execute(sentencia, [palabra])
    con.commit()

 def obtenerpalabra(): 
    consulta = "SELECT palabra FROM diccionario"
    cursor.execute(consulta)
    con.commit()
    return cursor.fetchall()
    

 def buscarsignificadopalabra(palabra):
    consulta = "SELECT significado FROM diccionario WHERE palabra = ?"
    cursor.execute(consulta,[palabra])
    con.commit()
    return cursor.fetchone() 
    
except Exception as e:
    print (e)

try:
 def principal():
    crear_tabla()
 menu = """
 === Bienvenido al diccionario ===
 a) agregar nueva palabra
 b) editar palabara existente
 c) eliminar palabra existente 
 d) ver listado de palabras
 e) buscar significado de palabra 
 f) salir 
 Elige: """
except Exception as e:
    print (e) 

while True:
 eleccion = input(menu)
 if eleccion == "a":
   palabra = input("ingresa la palabra: ")
   posible_significado = buscarsignificadopalabra(palabra)
   if posible_significado:
      print("la palabra\t"+ palabra +"\tya existe")
   else:
      significado = input("Ingrese el significado : ")
      agregar_palabra (palabra,significado)
      print("palabra agregada")
 elif eleccion == "b":
    palabra = input ("Ingresar la palabra que deseas editar: ")
    nuevosignificado = input ("Ingresar nuevo significado: ")
    editar_palabra(palabra, nuevosignificado)
    print("palabra actualizada")
 elif eleccion == "c":
     palabra = input ("Ingresar la palabra que desea eliminar: ")
     Eliminarpalabra(palabra)
     print ("la palabra\t" +palabra+"\tha sido eliminada")
 elif eleccion == "d":
   palabras = obtenerpalabra()
   print ("=== Listado de palabras ===")
   for palabra in palabras:
      print(palabra[0])
 elif eleccion == "e":
   palabra = input("Introdusca la palabra que desea saber el significado: ")
   significado = buscarsignificadopalabra(palabra)
   if significado:
      print (f"El significado de '{palabra}' es:\n{significado}")
   else:
      print(f"Palabra\t" + palabra + "\tno encontrada")
 elif eleccion == "f":
    print("Saliste del diccionario")
    break
 else:
    print("Eleccion invalida")
    
con.close