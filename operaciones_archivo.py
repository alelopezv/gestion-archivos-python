# Aquí creamos las funciones necesarias para crear un archivo, leer su contenido y agregar un mensaje al final del archivo

import os

def crear_archivo():
    with open("datos.txt", "w") as archivo:
        archivo.write("¡Bienvenido! Este es un archivo de prueba.\n")
    print("Archivo 'datos.txt' creado y escrito con éxito.")

def leer_lineas():
    try:
        with open("datos.txt", "r") as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("El archivo 'datos.txt' no se encontró.")

def leer_contenido():
    try:
        with open("datos.txt", "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)

        info = os.stat("datos.txt")
        print(f"Nombre del archivo: datos.txt")
        print(f"Tamaño del archivo: {info.st_size} bytes")
        print(f"Última modificación: {info.st_mtime}")

    except FileNotFoundError:
        print("El archivo 'datos.txt' no se encontró.")

def agregar_mensaje():
    with open("datos.txt", "a") as archivo:
        archivo.write("¡Este es un nuevo mensaje agregado al archivo!\n")
    print("Nuevo mensaje agregado al archivo 'datos.txt' con éxito.")