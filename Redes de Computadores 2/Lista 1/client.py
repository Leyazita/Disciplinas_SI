import socket
import time

# Configuração do servidor
server_ip_docker = 'server'
#server_ip_local = 'localhost'
server_port = 12345

# Criação do socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#time.sleep(5)

# Enviando 1000 mensagens para o servidor
for i in range(1000):
    # Criando a mensagem com a marcação de tempo
    message = str(time.time()).encode()

    # Enviando a mensagem para o servidor
    client_socket.sendto(message, (server_ip_docker, server_port))
