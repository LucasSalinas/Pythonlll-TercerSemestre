"""
Laboratorio 3: Clase 5
Lucas Salinas
Registros con Postgresql y Python
"""
import psycopg2

connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with connection:
        with connection.cursor() as cur:
            sentencia = 'DELETE FROM persona WHERE id_persona in %s'
            entrada = input('Digite los números de los registros que quiere eliminar(utilice coma): ')
            valores = (tuple(entrada.split(',')),)
            cur.executemany(sentencia, (valores,))
            registros_actualizados = cur.rowcount
            print(f'Registros ingresados: {registros_actualizados}')

except Exception as e:
    print(f'A ocurrido un error {e}')
finally:
    connection.close()
