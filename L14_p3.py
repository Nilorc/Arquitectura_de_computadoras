import random

def calcular_pi(muestras):
    muestras_in_circulo = 0

    for _ in range(muestras):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # calculamos una radio con los valores de x e y
        r = x**2 + y**2

        if r <= 1: # el radio debe ser menor que el radio del círculo
            muestras_in_circulo += 1

    # fórmula para calcular Pi 
    pi_aprox =  (muestras_in_circulo)*4 /muestras
    return pi_aprox

if __name__ == "__main__":
    muestras = 10000000
    pi = calcular_pi(muestras)

    print("El valor de Pi calculado es:", pi)

#3.b)
import random
import multiprocessing

def calcular_pi(muestras):
    muestras_in_circulo = 0

    for _ in range(muestras):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # calculamos una radio con los valores de x e y
        r = x**2 + y**2

        if r <= 1: # el radio debe ser menor que el radio del círculo
            muestras_in_circulo += 1

    # fórmula para calcular Pi 
    pi_aprox = (muestras_in_circulo)*4 / muestras
    return pi_aprox

if __name__ == "__main__":
    muestras = 10000000
    procesos = 4

    with multiprocessing.Pool(procesos) as p:
        resultados = p.map(calcular_pi, [muestras // procesos]*procesos)

    pi = 0
    for resultado in resultados:
        pi += resultado
    pi /= procesos

    print("El valor de Pi calculado es:", pi)
