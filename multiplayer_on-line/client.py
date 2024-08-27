import socket

# Configurações do Cliente
HOST = "127.0.0.1"  # Endereço IP do servidor (localhost)
PORT = 12345  # Porta do servidor

# Configuração de Rede
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    mensagem = client.recv(1024).decode("utf-8")
    print(mensagem)

    if "Escolha" in mensagem:
        jogada = input("Digite sua jogada: ")
        client.sendall(jogada.encode("utf-8"))
