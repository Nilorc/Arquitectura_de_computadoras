import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

"""
Función: calcular_histograma
Entrada: El archivo de la imagen en formato .npy
Salida: El arreglo del histograma
"""
def calcular_histograma(filename_npy):
    # Cargamos la imagen .npy a un arreglo bidimensional
    imagen = np.load(filename_npy)  # La variable imagen viene a ser un arreglo bidimensional como cualquier otro

    #Información útil: Calcular las filas y columnas de la matriz (largo y ancho de la imagen)
    M = len(imagen)     # Número de filas
    N = len(imagen[0])  # Número de columnas

     # Inicializamos un arreglo de ceros para el histograma
    histograma = np.zeros(256, dtype=int)

    # Iteramos sobre cada píxel de la imagen
    for i in range(M):
        for j in range(N):
            # Incrementamos el contador del valor del píxel en el histograma
            histograma[imagen[i, j]] += 1

    return histograma
   

"""
Función: graficar_histograma
Entradas:
- histograma_list: Su histograma que quiere graficar
- filename: Cadena de texto con el nombre del archivo para su gráfico que va a generar. Debe terminar en .png
- color: Cadena de texto con el color en inglés para su gráfico, 
Salida: Genera un gráfico de su histograma en formato .png
"""
def graficar_histograma(histograma_list, filename, color):
    plt.plot(range(0, len(histograma_list)), histograma_list, color=color)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

#funcion auxiliar para graficar y calcular el histograma de una sola imagen
def calcular_y_graficar(imagen):
    # Calculamos el histograma de la imagen
    histograma = calcular_histograma(imagen)
    # Graficamos el histograma
    graficar_histograma(histograma, f'{imagen}.png', 'blue')

if __name__ == '__main__':
    #nombres de las imagenes a utilizar
    imagenes = ['lena_x2.npy','hong kong_x2.npy','stonehenge_x2.npy','goldhill_x2.npy']
    inicio1 = time.perf_counter()
    for imagen in imagenes:
        calcular_y_graficar(imagen)
    fin1 = time.perf_counter()
    print("Tiempo de ejecucion en serie:", fin1 - inicio1)

    inicio2 = time.perf_counter()
    with Pool(processes = 4) as p:
        p.map(calcular_y_graficar, imagenes)
    fin2 = time.perf_counter()
    print('Tiempo de ejecucion en paralelo:', fin2 - inicio2)

    # Calculo del Speedup
    speedup = (fin1 - inicio1) / (fin2 - inicio2)
    print('Speedup:', speedup)


    #2.c)
    import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

"""
Función: calcular_histograma
Entrada: El archivo de la imagen en formato .npy
Salida: El arreglo del histograma
"""
def calcular_histograma(filename_npy):
    # Cargamos la imagen .npy a un arreglo bidimensional
    imagen = np.load(filename_npy)  # La variable imagen viene a ser un arreglo bidimensional como cualquier otro

    #Información útil: Calcular las filas y columnas de la matriz (largo y ancho de la imagen)
    M = len(imagen)     # Número de filas
    N = len(imagen[0])  # Número de columnas

     # Inicializamos un arreglo de ceros para el histograma
    histograma = np.zeros(256, dtype=int)

    # Iteramos sobre cada píxel de la imagen
    for i in range(M):
        for j in range(N):
            # Incrementamos el contador del valor del píxel en el histograma
            histograma[imagen[i, j]] += 1

    return histograma
   

"""
Función: graficar_histograma
Entradas:
- histograma_list: Su histograma que quiere graficar
- filename: Cadena de texto con el nombre del archivo para su gráfico que va a generar. Debe terminar en .png
- color: Cadena de texto con el color en inglés para su gráfico, 
Salida: Genera un gráfico de su histograma en formato .png
"""
def graficar_histograma(histograma_list, filename, color):
    plt.plot(range(0, len(histograma_list)), histograma_list, color=color)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

#funcion auxiliar para graficar y calcular el histograma de una sola imagen
def calcular_y_graficar(imagen):
    # Calculamos el histograma de la imagen
    histograma = calcular_histograma(imagen)
    # Graficamos el histograma
    graficar_histograma(histograma, f'{imagen}.png', 'blue')

if __name__ == '__main__':
    #nombres de las imagenes a utilizar
    imagenes = ['lena.npy','hong kong.npy','stonehenge.npy','goldhill.npy']
    inicio1 = time.perf_counter()
    for imagen in imagenes:
        calcular_y_graficar(imagen)
    fin1 = time.perf_counter()
    print("Tiempo de ejecucion en serie:", fin1 - inicio1)

    inicio2 = time.perf_counter()
    with Pool(processes = 4) as p:
        p.map(calcular_y_graficar, imagenes)
    fin2 = time.perf_counter()
    print('Tiempo de ejecucion en paralelo:', fin2 - inicio2)

    # Calculo del Speedup
    speedup = (fin1 - inicio1) / (fin2 - inicio2)
    print('Speedup:', speedup)


    #luego de correr el codigo de la parte anterior y este se puede notar que el speedup disminuye asi como los tiempos de ejecuion para las imagenes pequeñas
    #sin embargo el tiempo de jecucion en paralelo es ligeramente mayor que la ejecuion en serie para este ultimo caso eso debido a que como son menores pixeles
    #el tiempo que le toma a un proceso graficar la imagen es menor tanto que no hace mucha diferencia si se ejecuta para cada imagen o de una en una.