import socket
import time
import statistics

# Configuração do servidor
server_ip_docker = '0.0.0.0'
#server_ip_local = 'localhost'
server_port = 12345

# Criação do socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vinculação do IP e porta
server_socket.bind((server_ip_docker, server_port))

# Lista para armazenar os tempos de atraso
delays = []

# Loop para receber 1000 mensagens
for i in range(1000):
    # Recebendo a mensagem e o endereço do cliente
    message, address = server_socket.recvfrom(1024)

    # Calculando o atraso
    send_time = float(message.decode())
    delay = time.time() - send_time
    delays.append(delay)

# Calculando estatísticas
min_delay = min(delays)
max_delay = max(delays)
avg_delay = sum(delays) / len(delays)
std_dev_delay = statistics.stdev(delays)

print(f'Atraso Min: {min_delay}')
print(f'Atraso Max: {max_delay}')
print(f'Atraso Medio: {avg_delay}')
print(f'Atraso de Desvio Padrao: {std_dev_delay}')
