

#2.a)

import time
from urllib.request import urlopen

# Lista de URLs de las imágenes
urls = [
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/01.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/02.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/03.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/04.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/05.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/06.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/07.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/08.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/09.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/10.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/11.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/12.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/13.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/14.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/15.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/16.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/17.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/18.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/19.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/20.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/21.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/22.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/23.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/24.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/25.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/26.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/27.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/28.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/29.png'
]

inicio = time.perf_counter()

for i in range(1, len(urls) + 1):
    url = urls[i - 1]
    with urlopen(url) as page:
        image_data = page.read()  # data como objeto binario

        # Guardar la imagen en un archivo
        with open(f'image_{i}.png', 'wb') as f:
            f.write(image_data)

final = time.perf_counter()

print(f'Tiempo de ejecución: {final - inicio} segundos')


#2.b)
import time
import threading
from urllib.request import urlopen

# Lista de URLs de las imágenes
urls = [
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/01.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/02.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/03.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/04.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/05.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/06.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/07.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/08.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/09.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/10.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/11.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/12.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/13.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/14.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/15.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/16.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/17.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/18.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/19.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/20.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/21.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/22.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/23.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/24.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/25.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/26.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/27.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/28.png',
    'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/29.png'
]


def download_image(url, i):
    with urlopen(url) as page:
        image_data = page.read()  # data como objeto binario

        # Guardar la imagen en un archivo
        with open(f'image_{i}.png', 'wb') as f:
            f.write(image_data)

inicio = time.perf_counter()

threads = []
for i in range(1, len(urls) + 1):
    thread = threading.Thread(target=download_image, args=(urls[i - 1], i))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

final = time.perf_counter()

print(f'Tiempo de ejecución: {final - inicio} segundos')
