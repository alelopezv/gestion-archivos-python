# Sistema de Gestión de Archivos en Python

## 📖 Descripción

Este proyecto implementa un sistema básico de gestión de archivos utilizando Python.  
Permite crear, leer, modificar, renombrar y mover archivos, aplicando buenas prácticas como modularización, uso de funciones y manejo de excepciones.

El objetivo principal es demostrar el uso estructurado de funciones y módulos en un entorno práctico.

---

## Funcionalidades
- Creación de archivos
- Lectura por líneas y lectura completa
- Escritura y modo append
- Obtención de metadatos del archivo
- Renombrado de archivos
- Creación automática de carpetas
- Movimiento de archivos
- Manejo de excepciones (`FileNotFoundError`, `PermissionError`)

## Conceptos Aplicados
- Definición y uso de funciones
- Modularización en Python
- Manejo de archivos con `with open`
- Manejo de excepciones con `try/except/finally`
- Uso de módulos estándar (`os`, `shutil`)

## Estructura
- main.py → Archivo principal
- operaciones_archivo.py → Funciones para crear y leer archivos
- gestion_archivo.py → Funciones para renombrar y mover archivos

## ▶Cómo ejecutar
Desde la carpeta del proyecto:

```bash
python main.py