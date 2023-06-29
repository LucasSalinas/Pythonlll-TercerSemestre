"""
Laboratorio 3: Clase 2
Lucas Salinas
Manejo de archivos
"""
archivo1 = open('Prueba.txt', 'r', encoding='utf-8')

archivo2 = open('Copia.txt', 'a', encoding='utf-8')
archivo2.write(archivo1.read())
archivo1.close()
archivo2.close()