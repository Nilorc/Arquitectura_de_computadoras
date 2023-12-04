# Importando el módulo memory-profiler en el programa
from memory_profiler import profile

# Clase de decorador de perfil
@profile
# Una función predeterminada para verificar el uso de memoria
def defFunc():
    # Algunas variables aleatorias
    var1 = [1] * (6 ** 4)
    var2 = [1] * (2 ** 3)
    var3 = [2] * (4 * 6 ** 3)
    # Operaciones en la variable
    del var3
    del var1
    return var2

if __name__ == '__main__':
    # Llamando a la función predeterminada
    defFunc()

# Imprimir mensaje de confirmación
print("Hemos inspeccionado con éxito el uso de memoria desde la función predeterminada!")
