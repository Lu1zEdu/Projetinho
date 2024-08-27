import socket
import threading

# Configurações do Servidor
HOST = "127.0.0.1"  # Endereço IP do servidor (localhost)
PORT = 12345  # Porta do servidor

# Configurações de Rede
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)  # O servidor escuta até 2 conexões

clients = []
jogadas = {}


def gerenciar_cliente(client, address):
    print(f"Conexão estabelecida com {address}")
    client.sendall(
        "Bem-vindo ao Pedra, Papel, Tesoura! Aguardando outro jogador...\n".encode(
            "utf-8"
        )
    )

    # Aguarda o segundo jogador se conectar
    while len(clients) < 2:
        pass

    client.sendall("O jogo vai começar!\n".encode("utf-8"))

    while True:
        try:
            client.sendall("Escolha: Pedra, Papel ou Tesoura?\n".encode("utf-8"))
            jogada = client.recv(1024).decode("utf-8").strip().lower()
            jogadas[address] = jogada

            if len(jogadas) == 2:  # Se ambos os jogadores fizeram suas escolhas
                resultado = determinar_vencedor()
                for c in clients:
                    c.sendall(resultado.encode("utf-8"))
                jogadas.clear()  # Reinicia as jogadas para a próxima rodada
        except:
            clients.remove(client)
            client.close()
            break


def determinar_vencedor():
    jogador1, jogador2 = list(jogadas.values())
    if jogador1 == jogador2:
        return "Empate!\n"
    elif (
        (jogador1 == "pedra" and jogador2 == "tesoura")
        or (jogador1 == "papel" and jogador2 == "pedra")
        or (jogador1 == "tesoura" and jogador2 == "papel")
    ):
        return "Jogador 1 vence!\n"
    else:
        return "Jogador 2 vence!\n"


print("Servidor iniciado. Aguardando conexões...")
while True:
    client, address = server.accept()
    clients.append(client)
    thread = threading.Thread(target=gerenciar_cliente, args=(client, address))
    thread.start()
