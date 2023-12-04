# Importar la clase baseExtr desde el archivo memoryexample
from examplememory import baseExtr

if __name__ == "__main__":
    # URL de Git para importar la lista de palabras
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    # Array de palabras desde el archivo de texto
    array = ['cinco', 'cuatro', 'tres', 'dos', 'uno']
    # Inicializar un objeto Extractor desde la clase baseExtr()
    wordExtract = baseExtr()
    # Llamando a la función parseURL() desde la clase baseExtr
    wordExtract.parseURL(url)
    # Llamando a la función parseList()
    wordExtract.parseList(array)

"""En resumen, este código descarga el contenido de una URL y lo guarda en un archivo llamado 'url.txt',
y también escribe una lista de palabras en un archivo llamado 'wordParsing.txt'. 
Además, utiliza el módulo memory_profiler para realizar un seguimiento del uso de memoria 
durante la ejecución de las funciones decoradas con @profile"""