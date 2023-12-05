import requests
import time
import statistics

urls = [
    "https://www.wikipedia.org/",
    "https://www.nytimes.com/",
    "https://www.bbc.com/",
    "https://www.python.org/",
    "https://www.reddit.com/",
    "https://www.instagram.com/",
    "https://www.twitter.com/",
    "https://www.cnn.com/",
    "https://www.github.com/",
    "https://www.spotify.com/",
]

def save_html(url, indice):
    
    response = requests.get(url)
    if response.status_code == 200:
        # Crea un archivo con el nombre "pagina{indice}.html" y escribe el contenido HTML
        archivo = f"pagina{indice}.html"
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(response.text)


if __name__ == "__main__":
    
    tiempos = [] # para almacenar los tiempos
    # Repite la prueba cinco veces para obtener el tiempo mediano
    for _ in range(5):
        inicio_tiempo = time.perf_counter()

        # Descarga el HTML de cada URL y guarda en archivos
        for i in range(len(urls)):
            save_html(urls[i], i + 1)

        fin_tiempo = time.perf_counter()
        tiempo_total = fin_tiempo - inicio_tiempo
        tiempos.append(tiempo_total)

    # Calcula y muestra el tiempo mediano de ejecución
    tiempo_mediano = statistics.median(tiempos)
    print(f"Tiempo mediano de ejecución: {tiempo_mediano} segundos")

#2.b)
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import statistics

urls = [
    "https://www.wikipedia.org/",
    "https://www.nytimes.com/",
    "https://www.bbc.com/",
    "https://www.python.org/",
    "https://www.reddit.com/",
    "https://www.instagram.com/",
    "https://www.twitter.com/",
    "https://www.cnn.com/",
    "https://www.github.com/",
    "https://www.spotify.com/",
]


def descarga(url, indice) -> bool:
    response = requests.get(url)
    if response.status_code != 200:
        return False

    with open(f'pagina{indice}.html', 'w', encoding='utf-8') as f:
        f.write(response.text)

    return True

if __name__ == "__main__":
    tiempos = []
    workers = 3

    for _ in range(5):
        inicio = time.perf_counter()
        #para ejecutar descargas en paralelo
        with ThreadPoolExecutor(max_workers=workers) as executor:
            #iterar en las urls y asignar indices
            for i in range(len(urls)):
                # Enviar la tarea de descarga al ThreadPool
                executor.submit(descarga, urls[i], i + 1)

        fin = time.perf_counter()
        tiempo_total = fin - inicio
        tiempos.append(tiempo_total)

    tiempo_mediano = statistics.median(tiempos)
    print(f"Tiempo mediano de descarga: {tiempo_mediano} segundos")
