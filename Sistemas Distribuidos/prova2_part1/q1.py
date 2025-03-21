import numpy as np
import time
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Função para multiplicar duas submatrizes
def matrix_multiply(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

# Função para medir o tempo de execução usando MultiThreading
def multithreaded_multiplication(matrix_a, matrix_b, size):
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        result = list(executor.map(matrix_multiply, [matrix_a]*size, [matrix_b]*size))
    return time.time() - start_time

# Função para medir o tempo de execução usando MultiProcessing
def multiprocess_multiplication(matrix_a, matrix_b, size):
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        result = list(executor.map(matrix_multiply, [matrix_a]*size, [matrix_b]*size))
    return time.time() - start_time

# Função para testar o desempenho
def test_performance():
    sizes = list(range(2, 101, 10))
    thread_times = []
    process_times = []

    for size in sizes:
        matrix_a = np.random.rand(size, size)
        matrix_b = np.random.rand(size, size)

        # Teste com MultiThreading
        thread_time = multithreaded_multiplication(matrix_a, matrix_b, size)
        thread_times.append(thread_time)

        # Teste com MultiProcessing
        process_time = multiprocess_multiplication(matrix_a, matrix_b, size)
        process_times.append(process_time)

    # Plotando os resultados
    plt.plot(sizes, thread_times, label='MultiThread')
    plt.plot(sizes, process_times, label='MultiProcess')
    plt.xlabel("Matrix Size (NxN)")
    plt.ylabel("Time (s)")
    plt.title("Performance Comparison: MultiThread vs MultiProcess")
    plt.legend()
    plt.show()

# Condição principal para evitar problemas no Windows
if __name__ == '__main__':
    test_performance()
