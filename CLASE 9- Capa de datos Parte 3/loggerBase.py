"""
Laboratorio 3: Clase 8 y 9
Lucas Salinas
Capa de Datos Logging y Postgresql parte 2 y parte 3
"""
import logging as log
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])
if __name__ == '__main__':
    log.debug('Mensaje de debug')
    log.info('Mensaje de info')
    log.warning('Mensaje de warning')
    log.error('Mensaje de error')
    log.critical('Mensaje de critical')