import socket
import time
import matplotlib.pyplot as plt
import numpy as np

def simulate_clients(server_type, num_clients, repetitions):
    """
    Simula o envio de mensagens para o servidor.
    Retorna os tempos de resposta para o tipo de servidor especificado.
    """
    host = "127.0.0.1"
    port = 12345
    response_times = []

    for _ in range(repetitions):
        times = []
        for _ in range(num_clients):
            try:
                start_time = time.time()
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((host, port))
                client_socket.sendall(b"2024")
                client_socket.recv(1024)  # Recebe a resposta
                client_socket.close()
                times.append(time.time() - start_time)
            except Exception as e:
                print(f"Erro ao conectar: {e}")
        response_times.append(np.mean(times))  # Média dos tempos de resposta
    return response_times

# Simulação de diferentes clientes
if __name__ == "__main__":
    repetitions = 10
    client_counts = [10, 100, 1000, 10000]

    # Tempos médios de resposta por servidor
    sequential_times = {}
    concurrent_times = {}

    for num_clients in client_counts:
        # print(f"Simulando {num_clients} clientes para o servidor SEQUENCIAL...")
        # sequential_times[num_clients] = simulate_clients("sequential", num_clients, repetitions)

        print(f"Simulando {num_clients} clientes para o servidor CONCORRENTE...")
        concurrent_times[num_clients] = simulate_clients("concurrent", num_clients, repetitions)

    # Gráfico de Linha: Tempos Médios para o servidor sequencial
    # plt.figure(figsize=(10, 6))
    # for num_clients, times in sequential_times.items():
    #     plt.plot(
    #         range(1, repetitions + 1),
    #         times,
    #         label=f"Sequencial - {num_clients} clientes",
    #         marker="o",
    #     )
    # plt.title("Tempos Médios de Resposta - Servidor Sequencial")
    # plt.xlabel("Repetições")
    # plt.ylabel("Tempo Médio de Resposta (s)")
    # plt.legend()
    # plt.grid()
    # plt.show()

    # Gráfico de Linha: Tempos Médios para o servidor concorrente
    plt.figure(figsize=(10, 6))
    for num_clients, times in concurrent_times.items():
        plt.plot(
            range(1, repetitions + 1),
            times,
            label=f"Concorrente - {num_clients} clientes",
            marker="s",
        )
    plt.title("Tempos Médios de Resposta - Servidor Concorrente")
    plt.xlabel("Repetições")
    plt.ylabel("Tempo Médio de Resposta (s)")
    plt.legend()
    plt.grid()
    plt.show()

    # # Boxplot: Distribuição dos tempos para o servidor sequencial
    # all_sequential = [time for times in sequential_times.values() for time in times]
    # plt.figure(figsize=(8, 6))
    # plt.boxplot(
    #     all_sequential,
    #     labels=["Sequencial"],
    #     patch_artist=True,
    #     boxprops=dict(facecolor="lightblue", color="blue"),
    #     medianprops=dict(color="red"),
    # )
    # plt.title("Distribuição de Tempos de Resposta - Servidor Sequencial")
    # plt.ylabel("Tempo de Resposta (s)")
    # plt.show()

    # Boxplot: Distribuição dos tempos para o servidor concorrente
    all_concurrent = [time for times in concurrent_times.values() for time in times]
    plt.figure(figsize=(8, 6))
    plt.boxplot(
        all_concurrent,
        labels=["Concorrente"],
        patch_artist=True,
        boxprops=dict(facecolor="lightgreen", color="green"),
        medianprops=dict(color="red"),
    )
    plt.title("Distribuição de Tempos de Resposta - Servidor Concorrente")
    plt.ylabel("Tempo de Resposta (s)")
    plt.show()

