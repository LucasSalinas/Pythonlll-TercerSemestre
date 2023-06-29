"""
Laboratorio 3: Clase 1
Lucas Salinas
Exceptions
"""
from Excepcion import Exception
resultado = None
a = 0
try:
    b = 10
    resultado = b / a
except Exception as ex:
    print(f'Aquí hay un error: {ex}')
print(f'Resultado: {resultado}')
print('sigue el código...')

resultado2 = None
try:
    a = int(input('Ingrese un número: '))
    b = int(input('Ingrese otro número: '))
    resultado2 = a / b

except ZeroDivisionError as problemaEspecifico:
    print(f'Aquí hay un error especifico ZeroDivisionError: {problemaEspecifico}')
except Exception as problema:
    print(f'Aquí hay un error: {problema}')
else:
    print('El programa no tiene ningún error')
finally:
    print('La revisión a finalizado')
print(f'Resultado: {resultado2}')
print('sigue el código')

num = None
try:
    num = int(input('Ingrese un número: '))
    if num == 0:
        raise BusquedaException('Error, el número ingresado es menor a 0')
except Exception as problem:
    print(f'Error encontrado: {type(problem)}')
