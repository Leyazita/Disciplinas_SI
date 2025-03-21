import time

for i in range(10):
    t1 = time.time()  # Obter o tempo corrente
    time.sleep(10)  # Dormir por 10 segundos
    t2 = time.time()  # Obter o tempo corrente
    total = t2 - t1
    print(f"Execução {i + 1}: Tempo total = {total} segundos")