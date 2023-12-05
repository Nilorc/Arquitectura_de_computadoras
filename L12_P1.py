#copiar archivos

# 1. a)
def generar_archivos(M,N):
    for i in range(M):
        with open(f'./original/archivo{i + 1}', 'w') as f:
            f.write('f'*N) #segun condicion del problema N caracteres , yo escogí la letra f como caracter

#Se prueba para M = 3 y N = 1024
generar_archivos(3,1024)

# 1. b)
def copia_sincrona(M):
    for i in range(1,M+1):
         with open(f'./original/archivo{i}', 'r') as ar_original:
            with open(f'./copia/archivo{i}', 'w') as ar_copia:
                ar_copia.write(ar_original.read())

#se prueba para M = 3
copia_sincrona(3)

#1. c)
import asyncio

async def copia_asincrona(M):
    for i in range(1, M +1 ):
        with open(f'./original/archivo{i}', 'r') as ar_original:
            contenido = ar_original.read()
        with open(f'./copia/archivo{i}', 'w') as ar_copia:
            ar_copia.write(contenido)

#Probamos para el caso en el que hay solo 3 archivos en la carpeta original
asyncio.run(copia_asincrona(3))

#1.d)
import matplotlib.pyplot as plt
import time
import asyncio


def generar_archivos(M,N):
    for i in range(M):
        with open(f'./original/archivo{i + 1}', 'w') as f:
            f.write('f'*N) #segun condicion del problema N caracteres , yo escogí la letra f como caracter

def copia_sincrona(M):
    for i in range(1,M+1):
         with open(f'./original/archivo{i}', 'r') as ar_original:
            with open(f'./copia/archivo{i}', 'w') as ar_copia:
                ar_copia.write(ar_original.read())

async def copia_asincrona(M):
    for i in range(1, M +1 ):
        with open(f'./original/archivo{i}', 'r') as ar_original:
            contenido = ar_original.read()
        with open(f'./copia/archivo{i}', 'w') as ar_copia:
            ar_copia.write(contenido)

#Fijamos M = 3
M = 3
#Lista de los tamaños del archivo
lista_N = [2**i for i in range(10,26)]
#listas para almacenar los tiempos de ejecucion
tiempos_sync = []
tiempos_async = []

for N in lista_N:

    #Generamos los archivos
    generar_archivos(M,N)

    #Medimos el tiempo de la copia sincrona
    inicio = time.perf_counter()
    copia_sincrona(M)
    final = time.perf_counter()
    tiempo_medido = final - inicio
    tiempos_sync.append(tiempo_medido*1000) #se multiplica por 1000 para convertir a milisegundos

    #Medimos el tiempo de la copia asincrona
    inicio = time.perf_counter()
    asyncio.run(copia_asincrona(M))
    final = time.perf_counter()
    tiempo_medido = final - inicio
    tiempos_async.append(tiempo_medido*1000)

#Generamos la Gráfica
plt.plot(lista_N, tiempos_sync)
plt.plot(lista_N, tiempos_async)
plt.xlabel('File size [bytes]')
plt.ylabel('Copy time [ms]')
plt.legend(['Sync', 'Async'])
plt.savefig('SizeVsTime_1D.png')
plt.cla()
"""el tamaño del archivo afecta de forma directa al tiempo de ejecución, es decir cuanto más grande es el archivo,
 mayor es el tiempo que toma copiar su contenido a otra carpeta. Independientemente si es proceso es síncrono o asíncrono.
Esto se debe a que las operaciones de entrada y salida requieren una lectura de datos, la cual consiste en cargar los
datos del archivo a la memoria, si el archivo es muy grande se tardará más en cargar esos datos. Además, se requiere 
de una escritura de datos, es decir que se debe registrar el contenido del archivo en el disco, de forma similar si
hay muchos datos que escribir el tiempo que tomará este proceso será mayor."""
#1.e)
import matplotlib.pyplot as plt
import time
import asyncio

def generar_archivos(M,N):
    for i in range(M):
        with open(f'./original/archivo{i + 1}', 'w') as f:
            f.write('f'*N) #segun condicion del problema N caracteres , yo escogí la letra f como caracter

def copia_sincrona(M):
    for i in range(1,M+1):
         with open(f'./original/archivo{i}', 'r') as ar_original:
            with open(f'./copia/archivo{i}', 'w') as ar_copia:
                ar_copia.write(ar_original.read())

async def copia_asincrona(M):
    for i in range(1, M +1 ):
        with open(f'./original/archivo{i}', 'r') as ar_original:
            contenido = ar_original.read()
        with open(f'./copia/archivo{i}', 'w') as ar_copia:
            ar_copia.write(contenido)

# Lista de números de archivos
lista_M = list(range(2, 11))

# Listas para almacenar los tiempos de ejecución
tiempos_sync = []
tiempos_async = []

# Fijamos N = 2^20
N = 2**20

for M in lista_M:
    # Generamos los archivos
    generar_archivos(M, N)
    
    #Medimos el tiempo de la copia sincrona
    inicio = time.perf_counter()
    copia_sincrona(M)
    final = time.perf_counter()
    tiempo_medido = final - inicio
    tiempos_sync.append(tiempo_medido*1000) #se multiplica por 1000 para convertir a milisegundos
    
    #Medimos el tiempo de la copia asincrona
    inicio = time.perf_counter()
    asyncio.run(copia_asincrona(M))
    final = time.perf_counter()
    tiempo_medido = final - inicio
    tiempos_async.append(tiempo_medido*1000)

# Generamos la gráfica
plt.plot(lista_M, tiempos_sync)
plt.plot(lista_M, tiempos_async)
plt.xlabel('Numero de archivos [M]')
plt.ylabel('Copy time [ms]')
plt.legend(['Sync', 'Async'])
plt.savefig('MVsTime_1E.png')
plt.cla()
"""el número de archivos afecta de forma directa al tiempo de ejecución, es decir cuanto más grande es el archivo,
 mayor es el tiempo que toma copiar su contenido a otra carpeta. Esto se cumple tanto para el proceso asíncrono y síncrono, 
 pero no de manera uniforme. Esto se debe a que las operaciones de entrada y salida requieren una lectura y escritura de datos, 
 si hay muchos archivos leerlos y escribirlos tomará más tiempo.
Sin embargo, esto pude variar dependiendo de factores como la velocidad del disco o la cantidad de memoria disponible."""

