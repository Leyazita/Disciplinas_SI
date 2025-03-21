import socket
import time
import statistics

# Configurações do servidor
HOST = '0.0.0.0'
PORT = 65432

# Inicia o socket do servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        delays = []

        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            recv_time = time.time()
            sent_time = float(data.decode())
            
            delay = recv_time - sent_time
            delays.append(delay)

            if len(delays) == 1000:
                break

        min_delay = min(delays)
        max_delay = max(delays)
        avg_delay = statistics.mean(delays)
        std_dev_delay = statistics.stdev(delays)

        print("\nEstatísticas dos atrasos:")
        print(f"Atraso mínimo: {min_delay}s")
        print(f"Atraso máximo: {max_delay}s")
        print(f"Atraso médio: {avg_delay}s")
        print(f"Desvio-padrão do atraso: {std_dev_delay}s")
