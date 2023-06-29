"""
Laboratorio 3: Clase 2
Lucas Salinas
Manejo de archivos
"""
try:
    archivo1 = open('Prueba.txt', 'w', encoding='utf8')
    archivo1.write('Creo mi Archivo txt en Python\nLas diferentes letras en la creación de un archivo y su uso\nr -> '
                   'es para leer un archivo\na -> para agregar más info\nx -> crear un archivo\nt -> especifica que '
                   'el archivo es de texto\nb -> especifica que el tipo de archivo es binario\nw+ | r+ -> leer y '
                   'escribir')
except Exception as e:
    print(e)
finally:
    archivo1.close()
