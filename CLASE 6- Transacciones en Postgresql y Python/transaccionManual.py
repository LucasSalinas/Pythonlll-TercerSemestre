"""
Laboratorio 3: Clase 6
Lucas Salinas
Transacciones en Postgresql y Python
"""
import psycopg2

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    connection.autocommit = False
    cursor = connection.cursor()

    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Lucas', 'Salinas', 'lsalinas@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Silvina', 'Abeiro', 'sabeiro@gmail.com')
    cursor.execute(sentencia, valores)

    connection.commit()
    print('finalizo la transacción de datos')
except Exception as e:
    connection.rollback()
    print(f'A ocurrido un error se a identificado con el rollback: {e}')
finally:
    connection.close()
