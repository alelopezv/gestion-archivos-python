# Aquí importamos las funciones necesarias desde los módulos correspondientes

from operaciones_archivo import (
    crear_archivo,
    leer_lineas,
    leer_contenido,
    agregar_mensaje
)

from gestion_archivo import (
    renombrar_archivo,
    mover_a_backup,
    leer_archivo_movido
)

def main():
    crear_archivo()
    leer_lineas()
    leer_contenido()
    agregar_mensaje()
    renombrar_archivo()
    mover_a_backup()
    leer_archivo_movido()

if __name__ == "__main__":
    main()