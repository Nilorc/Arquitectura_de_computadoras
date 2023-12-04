import time
import multiprocessing as mp

# Definición de constantes
X6 = 10 ** 6  # 1 millón
X7 = 10 ** 7  # 10 millones

# Definición de la función worker
def worker(num, wait, amt=X6):
    """
    A function that allocates memory over time.
    """
    frame = []  # Inicializa una lista vacía llamada 'frame'

    # Proceso de asignación de memoria en el tiempo
    for idx in range(num):
        frame.extend([1] * amt)  # Agrega 'amt' elementos con valor '1' a la lista 'frame'
        time.sleep(wait)  # Espera durante 'wait' segundos

    del frame  # Elimina la lista 'frame' para liberar la memoria

# Verifica si el script está siendo ejecutado como el programa principal
if __name__ == '__main__':
    # Crea un objeto Pool de multiprocesamiento con 4 procesos
    pool = mp.Pool(processes=4)

    # Define una lista de tareas asincrónicas con diferentes conjuntos de argumentos
    tasks = [
        pool.apply_async(worker, args=(5, 5, X6)),
        pool.apply_async(worker, args=(5, 2, X7)),
        pool.apply_async(worker, args=(5, 5, X6)),
        pool.apply_async(worker, args=(5, 2, X7))
    ]

    # Espera a que todas las tareas asincrónicas se completen y recopila los resultados
    results = [p.get() for p in tasks]

"""En resumen, este script utiliza el módulo multiprocessing para ejecutar la función worker
 de manera asíncrona en varios procesos con diferentes conjuntos de argumentos, lo que simula
   la asignación de memoria en paralelo. La función worker agrega elementos a una lista y espera
     un tiempo específico para simular un proceso que consume recursos"""

"""Comandos para ejecutarlo"""

#mprof run -M python .\ejemplo2_myscript_multiporcess.py
#mprof plot