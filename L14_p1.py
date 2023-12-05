#1.a)
import time
from werkzeug.security import check_password_hash #INSTALE ESTA LIBERIA, tipee en su terminal: pip install Werkzeug
from multiprocessing import Pool

contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'

# Arreglo con las letras del abecedario
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#ya que nos dan de dato que las primeas letras son vocales entoces tambien es conveniente tener una arreglo de vocales
vocales = ['a', 'e','i','o','u']

def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

def probar_password():
	for letra1 in vocales:
		for letra2 in vocales:
			for letra3 in abecedario:
				contrasenha = letra1 + letra2 +letra3
				if comparar_con_password_correcto(contrasenha):
					return contrasenha


if __name__ == "__main__":
    inicio = time.perf_counter()
    contrasenha_correcta = probar_password()
    fin = time.perf_counter()
    print(f"La contraseña correcta es: {contrasenha_correcta}")
    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")
	

#1.b)
import time
from werkzeug.security import check_password_hash #INSTALE ESTA LIBERIA, tipee en su terminal: pip install Werkzeug
from multiprocessing import Pool

contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'

# Arreglo con las letras del abecedario
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#ya que nos dan de dato que las primeas letras son vocales entoces tambien es conveniente tener una arreglo de vocales
vocales = ['a', 'e','i','o','u']

def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

#como se asume que la primera letra es una vocal es necesaio modificar esta funcion
def probar_password(letra1):
	for letra2 in vocales:
		for letra3 in abecedario:
			contrasenha = letra1 + letra2 +letra3
			if comparar_con_password_correcto(contrasenha):
				return contrasenha

if __name__ == "__main__":
    proc = 5
    inicio = time.perf_counter()
    with Pool(processes=proc) as p:
        claves = p.map(probar_password, vocales)
    contrasenha_correcta = None #es necesario inicializar la variable con none porque aun no se encuentra la contraseña
    for palabra in claves:
        if palabra:
            contrasenha_correcta = palabra
            break
    fin = time.perf_counter()
    print(f"La contraseña correcta es: {contrasenha_correcta}")
    print(f"Tiempo de ejecucion en paralelo: {fin - inicio} segundos")