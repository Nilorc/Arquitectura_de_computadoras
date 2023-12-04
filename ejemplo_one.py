# Core Pkgs
import numpy as np
from memory_profiler import profile


@profile
def example_one():
    d = np.ones((100,1000,1000) )
    return d

if __name__ == '__main__':
    example_one()

    """ejecutar con:"""
    #python -m memory_profiler ejemplo_one.py

    """Para poder graficar previamente necesitamos este comando que crea una carpeta de coordenadas:"""
    #mprof run ejemplo_one.py
    """luego ejecutamos este comando que ploteara la ultima instrucion"""
    #mprof plot
    """PAra cambiarle el titulo del grafigo escribimos el siguiente comando"""
    #mprof plot -t "Mi_Grafica_memoria"
    """Para graficar en tramas continuas usamos este comando(opcional)"""
    #mprof plot -t "Mi_Grafica_memoria" --flame
