import socket
import threading

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 65432

# Lista de clientes conectados (nome e socket)
clients = []

# Função para tratar cada cliente
def handle_client(client_socket, username):
    while True:
        try:
            # Recebe a mensagem do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                if message.startswith('/exit'):
                    broadcast(f"{username} saiu do chat.", client_socket)
                    client_socket.send('/exit'.encode('utf-8'))
                    break
                else:
                    # Envia a mensagem para todos os clientes
                    broadcast(f"{username}: {message}", client_socket)
            else:
                break
        except:
            break
    
    # Remove o cliente ao desconectar
    remove_client(client_socket, username)

# Envia a mensagem para todos os clientes, exceto o remetente
def broadcast(message, sender_socket=None):
    for client, username in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client, username)

# Remove cliente da lista de clientes conectados
def remove_client(client_socket, username):
    for client, name in clients:
        if client == client_socket:
            clients.remove((client_socket, username))
            print(f"{username} desconectado.")
            client_socket.close()
            break

# Função para iniciar o servidor
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Servidor iniciado em {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        
        # Solicita o nome do usuário
        client_socket.send("Digite seu nome: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')
        clients.append((client_socket, username))
        
        print(f"{username} conectado de {addr}")
        broadcast(f"{username} entrou no chat.", client_socket)
        
        # Inicia uma thread para gerenciar esse cliente
        thread = threading.Thread(target=handle_client, args=(client_socket, username))
        thread.start()

if __name__ == "__main__":
    start_server()
