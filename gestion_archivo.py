# Aquí renombramos el archivo, lo movemos a una carpeta de backup y luego leemos su contenido

import os
import shutil

def renombrar_archivo():
    if os.path.exists("datos.txt"):
        os.rename("datos.txt", "datos_renombrados.txt")
        print("Archivo renombrado a 'datos_renombrados.txt' con éxito.")
    else:
        print("El archivo 'datos.txt' no se encontró para renombrar.")


def mover_a_backup():
    if not os.path.exists("backup"):
        os.makedirs("backup")

    shutil.move("datos_renombrados.txt", "backup/datos_renombrados.txt")
    print("Archivo movido a la carpeta 'backup' con éxito.")


def leer_archivo_movido():
    try:
        with open("backup/datos_renombrados.txt", "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo movido:")
            print(contenido)

    except FileNotFoundError:
        print("El archivo no se encontró.")
    except PermissionError:
        print("No tienes permiso para leer el archivo.")
    finally:
        print("Operación de lectura del archivo finalizada.")