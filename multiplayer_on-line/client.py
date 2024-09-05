import socket
import threading
import time

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 65432

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == '/exit':
                print("Você foi desconectado.")
                client_socket.close()
                break
            print(f"\n{message}")
        except:
            print("Erro de conexão. Saindo...")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Recebendo o pedido para o nome
    username = input(client_socket.recv(1024).decode('utf-8'))
    client_socket.send(username.encode('utf-8'))

    # Inicia uma thread para receber mensagens
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Loop para enviar mensagens
    while True:
        message = input()
        if message:
            client_socket.send(message.encode('utf-8'))
            if message.startswith('/exit'):
                print("Saindo do chat...")
                break

    # Espera a thread de recebimento terminar e fecha o socket
    receive_thread.join()
    client_socket.close()

if __name__ == "__main__":
    start_client()
