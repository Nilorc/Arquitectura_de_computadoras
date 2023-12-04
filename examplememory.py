# Importar el módulo memory_profiler
from memory_profiler import profile
# Importar el módulo requests en el programa
import requests

# Crear una clase base de extractor
class baseExtr:
    # Usar el decorador de perfil para monitorear el uso de memoria
    @profile
    # Función predeterminada para analizar palabras de una lista
    def parseList(self, array):
        # Crear un objeto de tipo archivo en el sistema
        sampleFile = open('wordParsing.txt', 'w')
        # Recorrer el archivo con un bucle for
        for parsedWords in array:
            # Escribir palabras en el archivo de ejemplo
            sampleFile.writelines(parsedWords)

    @profile
    # Otra función predeterminada para obtener URL
    def parseURL(self, url):
        # Obtener la respuesta del archivo
        response = requests.get(url).text
        with open('url.txt', 'w') as sampleFile:
            # Escribir las respuestas obtenidas en el archivo de ejemplo
            sampleFile.writelines(response)
