import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import os
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Variáveis globais
REQUESTS = [100, 1000, 10000, 100000]
PATH = '/index.html'
OUTPUT_DIR = '/app/output'
SEQUENCIAL_HOST = 'servidor_sequencial'
SEQUENCIAL_PORT = 8080
PARALELO_HOST = 'servidor_paralelo'
PARALELO_PORT = 8081


def make_request(host, port, path):
    """Faz uma requisição HTTP GET para o host e porta especificados."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        client_socket.sendall(request.encode('utf-8'))
        response = client_socket.recv(4096)
    return response


def measure_response_times(host, port, path, num_requests):
    """Mede os tempos de resposta para um número especificado de requisições."""
    times = []
    for _ in range(num_requests):
        start_time = time.time()
        try:
            make_request(host, port, path)
            end_time = time.time()
            times.append(end_time - start_time)
        except ConnectionRefusedError as e:
            logging.error(f"Erro de conexão ao servidor {host}:{port}: {e}")
            return None
    return times


def save_plot(times, label, num_requests, output_dir):
    """Salva o gráfico de tempos de resposta."""
    plt.plot(times, label=label)
    plt.xlabel('Requisição')
    plt.ylabel('Tempo de Resposta (s)')
    plt.title(f'Tempo de Resposta para {num_requests} Requisições - {label}')
    plt.legend()
    plt.savefig(f'{output_dir}/{num_requests}_requests_{label.lower()}.png', dpi=300)
    plt.clf()


def save_comparison_plot(avg_times_sequencial, avg_times_paralelo, output_dir):
    """Salva o gráfico comparativo de tempos médios de resposta."""
    bar_width = 0.35
    index = np.arange(len(REQUESTS))
    
    plt.bar(index, avg_times_sequencial, bar_width, label='Sequencial')
    plt.bar(index + bar_width, avg_times_paralelo, bar_width, label='Paralelo')
    
    plt.xlabel('Número de Requisições')
    plt.ylabel('Tempo Médio de Resposta (s)')
    plt.title('Comparação dos Tempos Médios de Resposta - Sequencial vs Paralelo')
    plt.xticks(index + bar_width / 2, [str(r) for r in REQUESTS])
    plt.legend()
    plt.savefig(f'{output_dir}/comparison_avg_response_times.png', dpi=300)
    plt.clf()


def run_tests():
    """Executa os testes de desempenho e gera gráficos comparativos."""
    avg_times_sequencial = []
    avg_times_paralelo = []

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    logging.info("Aguardando para garantir que os servidores estejam prontos...")
    time.sleep(10)

    for num_requests in REQUESTS:
        logging.info(f"Testando com {num_requests} requisições...")

        sequencial_times = measure_response_times(SEQUENCIAL_HOST, SEQUENCIAL_PORT, PATH, num_requests)
        if not sequencial_times:
            continue

        paralelo_times = measure_response_times(PARALELO_HOST, PARALELO_PORT, PATH, num_requests)
        if not paralelo_times:
            continue

        save_plot(sequencial_times, 'Sequencial', num_requests, OUTPUT_DIR)
        save_plot(paralelo_times, 'Paralelo', num_requests, OUTPUT_DIR)

        avg_times_sequencial.append(np.mean(sequencial_times))
        avg_times_paralelo.append(np.mean(paralelo_times))

    if avg_times_sequencial and avg_times_paralelo:
        save_comparison_plot(avg_times_sequencial, avg_times_paralelo, OUTPUT_DIR)


if __name__ == "__main__":
    run_tests()
