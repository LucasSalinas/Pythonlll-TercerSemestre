"""
Laboratorio 3: Clase 2
Lucas Salinas
Manejo de archivos
"""
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('Prueba.txt') as archivo:
    print(archivo.read())
