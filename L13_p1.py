""" Desarrolle una conexión cliente-servidor usando sockets
que permita hacer pedidos dependiendo si hay stock."""

"""a) Desarrolle el cliente.py (2 pt)
b) Desarrolle una función para manejar la conexión con un cliente dentro de
servidor.py. (2 pt)
c) Desarrollar el servidor.py (2 pt)
d) Responder en el pdf: ¿Es necesario el uso de locks? ¿Por qué?"""

#Cliente
import socket

SOCK_BUFFER = 1024

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a {server_address[0]}:{server_address[1]}")



    sock.connect(server_address)
    try:
        while True:
            producto = input('Ingrese el nombre de un electrodoméstico: ')
            sock.sendall(producto.encode('utf-8'))
            data = sock.recv(SOCK_BUFFER)
            if data.decode('utf-8') == '1':
                print('Producto en stock. Pedido procesado.')
            else:
                print('Producto agotado. Pedido no procesado.')
    finally:
        print("Cerrando conexión")
        sock.close()



if __name__ == "__main__":
    main()


#server
import socket
import threading

SOCK_BUFFER = 1024
stock = {"lavadora": 5, "refrigerador": 3, "aspiradora": 2, "licuadora": 4}

stock_lock = threading.Lock() #es necesario el lock para evitar las condiciones de carrera al modificar el inventario

def manejar_client(conn):
    try:
        while True:
            producto = conn.recv(SOCK_BUFFER).decode('utf-8')
            # Adquirir el lock antes de modificar el inventario
            with stock_lock:
                if stock[producto] > 0:
                    conn.sendall('1'.encode('utf-8'))
                    stock[producto] -= 1
                else:
                    conn.sendall('0'.encode('utf-8'))
    except ConnectionResetError:
        print("El cliente ha cerrado abruptamente la conexión")
    finally:
        print("El cliente ha cerrado la conexión")
        conn.close()

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Iniciando servidor en IP {server_address[0]} y puerto {server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        print(f"Conexion desde {client_address[0]}:{client_address[1]}")
        client_thread = threading.Thread(target=manejar_client, args=(conn,))
        client_thread.start()
