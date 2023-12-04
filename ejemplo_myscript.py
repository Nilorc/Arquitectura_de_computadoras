import time

# Definición de constantes
X6 = 10 ** 6  # 1 millón
X7 = 10 ** 7  # 10 millones

# Definición de la función worker
def worker(num, wait, amt=X6):
    """
    A function that allocates memory over time.
    """
    frame = []  # Inicializa una lista vacía llamada 'frame'

    for idx in range(num):
        frame.extend([1] * amt)  # Agrega 'amt' elementos con valor '1' a la lista 'frame'
        time.sleep(wait)  # Espera durante 'wait' segundos

    del frame  # Elimina la lista 'frame' para liberar la memoria

# Bloque principal de ejecución
if __name__ == '__main__':
    # Llamadas a la función worker con diferentes argumentos
    worker(5, 5, X6)  # Realiza 5 iteraciones, espera 5 segundos y agrega 1 millón de elementos en cada iteración
    worker(5, 2, X7)  # Realiza 5 iteraciones, espera 2 segundos y agrega 10 millones de elementos en cada iteración
    worker(5, 5, X6)  # Realiza 5 iteraciones, espera 5 segundos y agrega 1 millón de elementos en cada iteración
    worker(5, 2, X7)  # Realiza 5 iteraciones, espera 2 segundos y agrega 10 millones de elementos en cada iteración
