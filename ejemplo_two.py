# Core Pkgs
import numpy as np
from memory_profiler import profile


@profile(precision=4) #precision se usa para ver la cantidad de decimales
def example_one():
    d = np.ones((100,1000,1000) )
    return d

#Guardar la salida
fp = open("report_mem.log","w+")


@profile(stream=fp) #guardará este perfil en el archivo report
def example_two():
    d = np.ones((100,1000,1000) )
    s = sum(d)
    return s

if __name__ == '__main__':
    example_one()
    example_two()



    """ejecutar con:"""
    #python -m memory_profiler ejemplo_two.py

    """Para poder graficar previamente necesitamos este comando que crea una carpeta de coordenadas:"""
    #mprof run ejemplo_two.py
    """luego ejecutamos este comando que ploteara la ultima instrucion"""
    #mprof plot
    """PAra cambiarle el titulo del grafigo escribimos el siguiente comando"""
    #mprof plot -t "Mi_Grafica_memoria"
    """Para graficar en tramas continuas usamos este comando(opcional)"""
    #mprof plot -t "Mi_Grafica_memoria" --flame
