#asincrono
import numpy as np
import time

def manhattan_distance(a, b):
    return np.sum(np.abs(a-b))

# Generar vectores aleatorios de tamaño 4096
np.random.seed(0)
a = np.random.randint(low=-2147483648, high=2147483647, size=4096, dtype=np.int32)
b = np.random.randint(low=-2147483648, high=2147483647, size=4096, dtype=np.int32)

# Calcular la distancia de Manhattan y el tiempo de ejecución
start_time = time.time()
dist = manhattan_distance(a, b)
end_time = time.time()

print(f"Distancia de Manhattan: {dist}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")



#v2.
"""import numpy as np
import time

def sincrono(arreglo1,arreglo2):
    length=len(arreglo1)
    suma=0
    for i in range(length):
        suma+=abs(arreglo2[i]-arreglo1[i])
    return suma


if __name__=='__main__':
    arreglo1=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    arreglo2=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    listaTiempos=[]
    for i in range(100):
        t=time.perf_counter()
        sincrono(arreglo1,arreglo2)
        listaTiempos.append(time.perf_counter()-t)
    print(f"La mediana de los tiempos de ejecución del programa de forma síncrona es de {np.median(listaTiempos)} segundos.")"""

#uando multihilo
import numpy as np
import time
import threading

def manhattan_distance(a, b, start, end, result, index):
    result[index] = np.sum(np.abs(a[start:end]-b[start:end]))

# Generar vectores aleatorios de tamaño 4096
np.random.seed(0)
a = np.random.randint(low=-2147483648, high=2147483647, size=4096, dtype=np.int32)
b = np.random.randint(low=-2147483648, high=2147483647, size=4096, dtype=np.int32)

# Número de hilos
num_threads = 4

# Crear listas para almacenar los hilos y los resultados
threads = [None] * num_threads
results = [None] * num_threads

# Calcular la distancia de Manhattan y el tiempo de ejecución
start_time = time.time()

# Crear y empezar los hilos
for i in range(num_threads):
    start = i * len(a) // num_threads
    end = (i + 1) * len(a) // num_threads
    threads[i] = threading.Thread(target=manhattan_distance, args=(a, b, start, end, results, i))
    threads[i].start()

# Esperar a que todos los hilos terminen
for i in range(num_threads):
    threads[i].join()

# Sumar los resultados de todos los hilos
dist = sum(results)

end_time = time.time()

print(f"Distancia de Manhattan: {dist}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")


"""import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

#No se cambian los arreglos por iteración ya que sino cada medición del tiempo involucraría un diferente cálculo. Deben estar en igualdad de condiciones.

def multiHilo(arreglo1,arreglo2,hilos):
    return sum(list(PoolThreads.map(multiHiloAux,[[arreglo1,arreglo2,i,hilos] for i in range(hilos)])))

#Se usó la función .map tomando como argumento a un solo parámetro de entrada pero que conforma una lista con todos los argumentos necesarios.

def multiHiloAux(args):
    arreglo1,arreglo2,inicio,hilos=args #Se desempaquetan los argumentos
    length=len(arreglo1)
    suma=0
    for i in range(inicio,length,hilos):
        suma+=abs(arreglo2[i]-arreglo1[i])
    return suma

if __name__=='__main__':
    arreglo1=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    arreglo2=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    cantHilos=[1,2,4,8,16]
    for hilos in cantHilos:
        listaTiempos=[]
        PoolThreads=ThreadPoolExecutor(max_workers=hilos)
        for i in range(100):
            t=time.perf_counter()
            multiHilo(arreglo1,arreglo2,hilos)
            listaTiempos.append(time.perf_counter()-t)
        print(f"La mediana de los tiempos de ejecución del programa al emplear {hilos} hilos es de {np.median(listaTiempos)} segundos.")

"""

#usando multiproceso
import numpy as np
import time
import multiprocessing

def manhattan_distance(a, b, start, end, result, index):
    result[index] = np.sum(np.abs(a[start:end]-b[start:end]))

# Generar vectores aleatorios de tamaño 4096
np.random.seed(0)
a = np.random.randint(low=-2147483648, high=2147483647, size=4096, dtype=np.int32)
b = np.random.randint(low=-2147483648, high=2147483647, size=4096, dtype=np.int32)

# Número de procesos
num_processes = 4

# Crear un arreglo compartido para almacenar los resultados
result = multiprocessing.Array('i', num_processes)

# Calcular la distancia de Manhattan y el tiempo de ejecución
start_time = time.time()

# Crear y empezar los procesos
processes = []
for i in range(num_processes):
    start = i * len(a) // num_processes
    end = (i + 1) * len(a) // num_processes
    p = multiprocessing.Process(target=manhattan_distance, args=(a, b, start, end, result, i))
    p.start()
    processes.append(p)

# Esperar a que todos los procesos terminen
for p in processes:
    p.join()

# Sumar los resultados de todos los procesos
dist = sum(result)

end_time = time.time()

print(f"Distancia de Manhattan: {dist}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")



"""import numpy as np
import time
from multiprocessing import Pool

#No se cambian los arreglos por iteración ya que sino cada medición del tiempo involucraría un diferente cálculo. Deben estar en igualdad de condiciones.

def multiProcess(arreglo1,arreglo2,procesos):
    return sum(PoolProcess.starmap(multiProcessAux,([arreglo1,arreglo2,i,procesos] for i in range(procesos))))

def multiProcessAux(arreglo1,arreglo2,inicio,procesos):
    length=len(arreglo1)
    suma=0
    for i in range(inicio,length,procesos):
        suma+=abs(arreglo2[i]-arreglo1[i])
    return suma

if __name__=='__main__':
    cantProcesos=[1,2,4,8,16]
    arreglo1=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    arreglo2=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    for procesos in cantProcesos:
        listaTiempos=[]
        PoolProcess=Pool(processes=procesos)
        for i in range(100):
            t=time.perf_counter()
            multiProcess(arreglo1,arreglo2,procesos)
            listaTiempos.append(time.perf_counter()-t)
        print(f"La mediana de los tiempos de ejecución del programa al emplear {procesos} procesos es de {np.median(listaTiempos)} segundos.")
        PoolProcess.close()
        PoolProcess.join()

#Se cierra el Pool de Procesos por cada iteración debido a que la cantidad de procesos a evaluar va cambiando.
#Si no se cerrara, estos procesos seguirían activos y ello haría que el rendimiento del programa empeore al tener procesos trabajando en nada."""



#para calcular el speed up
# Tiempo de ejecución de la versión síncrona
time_sync = ...

# Tiempo de ejecución de la versión multihilo
time_multithread = ...

# Tiempo de ejecución de la versión multiproceso
time_multiprocess = ...

# Calcular SpeedUp
speedup_multithread = time_sync / time_multithread
speedup_multiprocess = time_sync / time_multiprocess

print(f"SpeedUp Multihilo: {speedup_multithread}")
print(f"SpeedUp Multiproceso: {speedup_multiprocess}")
